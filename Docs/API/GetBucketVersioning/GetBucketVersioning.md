> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketVersioning.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketVersioning

> **Note**
>
> This operation is not supported for directory buckets.

Returns the versioning state of a bucket.

To retrieve the versioning state of a bucket, you must be the bucket owner.

This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete status is `enabled`, the bucket owner must use an authentication device to change the versioning state of the bucket.

The following operations are related to `GetBucketVersioning`:

- [GetObject](../GetObject/GetObject.md)
- [PutObject](../PutObject/PutObject.md)
- [DeleteObject](../DeleteObject/DeleteObject.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?versioning HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the bucket for which to get the versioning information.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration>
   <Status>string</Status>
   <MfaDelete>string</MfaDelete>
</VersioningConfiguration>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [VersioningConfiguration](#response-syntax)

Root level tag for the VersioningConfiguration parameters.

Required: Yes

### [MFADelete](#response-syntax)

Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.

Type: String

Valid Values: `Enabled | Disabled`

### [Status](#response-syntax)

The versioning state of the bucket.

Type: String

Valid Values: `Enabled | Suspended`

## Examples

### Example

This example returns the versioning state of `amzn-s3-demo-bucket`.

```http
         GET /?versioning HTTP/1.1
         Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
         Date: Wed, 12 Oct 2009 17:50:00 GMT
         Authorization: authorization string
         Content-Type: text/plain
```

### Example

There are three versioning states:

If you enabled versioning on a bucket, the response is:

```xml
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Enabled</Status>
     </VersioningConfiguration>
```

### Example

If you suspended versioning on a bucket, the response is:

```xml
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Suspended</Status>
     </VersioningConfiguration>
```

### Example

If you never enabled (or suspended) versioning on a bucket, the response is:

```xml
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"/>
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- AWS Command Line Interface V2
- AWS SDK for .NET V4
- AWS SDK for C++
- AWS SDK for Go v2
- AWS SDK for Java V2
- AWS SDK for JavaScript V3
- AWS SDK for Kotlin
- AWS SDK for PHP V3
- AWS SDK for Python (Boto3)
- AWS SDK for Ruby V3
