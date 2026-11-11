#!/usr/bin/env python3
"""Serve the offline S3 API reference over MCP stdio."""

import json
import sys

if __package__:
    from .s3_docs import MAX_SEARCH_RESULTS, get_operation, list_operations, search_docs
else:
    from s3_docs import MAX_SEARCH_RESULTS, get_operation, list_operations, search_docs


LEGACY_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
MODERN_VERSION = "2026-07-28"
META = "io.modelcontextprotocol/"
SERVER_INFO = {"name": "s3-docs", "version": "1.0.0"}
CAPABILITIES = {"tools": {}}
INSTRUCTIONS = (
    "Use get_operation for a known Amazon S3 API operation and search_docs for discovery. "
    "Prefer English API terms, headers, and error codes when searching. Cite the returned "
    "local source and section. Distinguish documented behavior from implementation proposals."
)


def tool_definition(handler, description, properties, required=()):
    return {
        "name": handler.__name__,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": properties,
            "required": list(required),
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": True, "openWorldHint": False},
    }


TOOLS = {
    list_operations: tool_definition(
        list_operations,
        "List S3 API operation names in the offline reference.",
        {"prefix": {"type": "string", "description": "Optional case-insensitive name prefix."}},
    ),
    search_docs: tool_definition(
        search_docs,
        "Search the offline reference by name, header, error code, or keywords. "
        "Returns matching sections with source paths and short excerpts.",
        {
            "query": {"type": "string", "minLength": 1, "description": "Search terms, preferably in English."},
            "limit": {"type": "integer", "minimum": 1, "maximum": MAX_SEARCH_RESULTS, "default": 5},
        },
        ("query",),
    ),
    get_operation: tool_definition(
        get_operation,
        "Read a local S3 API article or a section by heading, including its subsections.",
        {
            "name": {"type": "string", "minLength": 1, "description": "Operation name, e.g. GetObject."},
            "section": {"type": "string", "description": "Optional heading, e.g. Request Syntax."},
        },
        ("name",),
    ),
}
HANDLERS = {handler.__name__: handler for handler in TOOLS}


class RpcError(Exception):
    def __init__(self, code, message, **details):
        super().__init__(message)
        self.payload = {"code": code, "message": message, **details}


def validate_arguments(arguments, schema):
    properties = schema["properties"]
    if missing := set(schema["required"]) - arguments.keys():
        raise ValueError(f"Missing argument(s): {', '.join(sorted(missing))}")
    if unknown := arguments.keys() - properties.keys():
        raise ValueError(f"Unknown argument(s): {', '.join(sorted(unknown))}")
    for name, value in arguments.items():
        field = properties[name]
        if field["type"] == "string":
            if not isinstance(value, str) or len(value) < field.get("minLength", 0):
                raise ValueError(f"{name} must be a string of at least {field.get('minLength', 0)} characters.")
        elif type(value) is not int or not field["minimum"] <= value <= field["maximum"]:
            raise ValueError(f"{name} must be an integer from {field['minimum']} to {field['maximum']}.")


def call_tool(params):
    name = params.get("name")
    if not isinstance(name, str) or name not in HANDLERS:
        raise RpcError(-32602, "Unknown tool. Use tools/list to discover available tools.")
    arguments = params.get("arguments", {})
    if not isinstance(arguments, dict):
        raise RpcError(-32602, "Tool arguments must be an object.")

    handler = HANDLERS[name]
    is_error = False
    try:
        validate_arguments(arguments, TOOLS[handler]["inputSchema"])
        value = handler(**arguments)
        message = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    except ValueError as error:
        is_error = True
        message = str(error)
    except OSError as error:
        print(f"{name}: {error}", file=sys.stderr)
        is_error = True
        message = "Could not read the local reference. Check that the repository clone is complete."
    return {"content": [{"type": "text", "text": message}], "isError": is_error}


class StdioSession:
    def __init__(self):
        self.legacy_initialized = False

    def dispatch(self, method, params):
        if method == "initialize":
            version = params.get("protocolVersion")
            if not isinstance(version, str):
                raise RpcError(-32602, "initialize requires protocolVersion.")
            self.legacy_initialized = True
            return {
                "protocolVersion": version if version in LEGACY_VERSIONS else LEGACY_VERSIONS[0],
                "serverInfo": SERVER_INFO,
                "capabilities": CAPABILITIES,
                "instructions": INSTRUCTIONS,
            }

        metadata = params.get("_meta", {})
        if not isinstance(metadata, dict):
            raise RpcError(-32602, "_meta must be an object.")
        version = metadata.get(META + "protocolVersion")
        modern = (
            method == "server/discover"
            or META + "protocolVersion" in metadata
            or (not self.legacy_initialized and method != "ping")
        )
        if modern:
            if not isinstance(version, str) or not isinstance(metadata.get(META + "clientCapabilities"), dict):
                raise RpcError(-32602, "Missing MCP protocolVersion or clientCapabilities in _meta.")
            if version != MODERN_VERSION:
                raise RpcError(-32022, "Unsupported protocol version", data={
                    "supported": [MODERN_VERSION], "requested": version,
                })

        result: dict[str, object]
        if method == "server/discover":
            result = {
                "supportedVersions": [MODERN_VERSION],
                "_meta": {META + "serverInfo": SERVER_INFO},
                "capabilities": CAPABILITIES,
                "instructions": INSTRUCTIONS,
                "ttlMs": 0,
                "cacheScope": "private",
            }
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": list(TOOLS.values())}
            if modern:
                result.update(ttlMs=0, cacheScope="private")
        elif method == "tools/call":
            result = call_tool(params)
        else:
            raise RpcError(-32601, "Method not found.")
        if modern:
            result["resultType"] = "complete"
        return result


def handle_line(line, session):
    response = {"jsonrpc": "2.0", "id": None}
    try:
        try:
            request = json.loads(line.decode("utf-8"))
        except (ValueError, RecursionError):
            raise RpcError(-32700, "Parse error.") from None
        if not isinstance(request, dict):
            raise RpcError(-32600, "Invalid request.")

        request_id = request.get("id")
        if type(request_id) in (str, int):
            response["id"] = request_id
        method = request.get("method")
        if request.get("jsonrpc") != "2.0" or not isinstance(method, str):
            raise RpcError(-32600, "Invalid request.")
        if "id" not in request:
            return None
        if response["id"] is None:
            raise RpcError(-32600, "Request ID must be a string or integer.")
        params = request.get("params", {})
        if not isinstance(params, dict):
            raise RpcError(-32602, "Params must be an object.")
        response["result"] = session.dispatch(method, params)
    except RpcError as error:
        response["error"] = error.payload
    return response


def main():
    session = StdioSession()
    for line in sys.stdin.buffer:
        response = handle_line(line, session)
        if response is not None:
            sys.stdout.buffer.write(json.dumps(response).encode("utf-8") + b"\n")
            sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
