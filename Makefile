PYTHON ?= python3
OPERATIONS ?=
IMPORTER = scripts/import_s3_api.py

.PHONY: help install import convert check

help:
	@printf '%s\n' \
		'make install  Install Python dependencies from requirements.txt' \
		'make import   Download AWS articles and save them as Markdown' \
		'make convert  Convert local HTML snapshots to Markdown' \
		'make check    Validate local Markdown without changing files' \
		'Set OPERATIONS="ListObjectsV2 GetObject" to select operations.' \
		'Set PYTHON=/path/to/python3 to use a different interpreter.'

install: requirements.txt
	@if [ -n "$$(sed '/^[[:space:]]*#/d; /^[[:space:]]*$$/d' "$<")" ]; then \
		"$(PYTHON)" -m pip --disable-pip-version-check install -r "$<"; \
	else \
		printf '%s\n' 'No third-party Python dependencies.'; \
	fi

import:
	"$(PYTHON)" -B $(IMPORTER) $(OPERATIONS)

convert:
	"$(PYTHON)" -B $(IMPORTER) --convert-local $(OPERATIONS)

check:
	"$(PYTHON)" -B $(IMPORTER) --check $(OPERATIONS)
