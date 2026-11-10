> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_PutBucketAbac.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# PutBucketAbac

Sets the attribute-based access control (ABAC) property of the general purpose bucket. You must have `s3:PutBucketABAC` permission to perform this action. When you enable ABAC, you can use tags for access control on your buckets. Additionally, when ABAC is enabled, you must use the TagResource and UntagResource actions to manage tags on your buckets. You can nolonger use the [PutBucketTagging](../PutBucketTagging/PutBucketTagging.md) and [DeleteBucketTagging](../DeleteBucketTagging/DeleteBucketTagging.md) actions to tag your bucket. For more information, see Enabling ABAC in general purpose buckets.

## Request Syntax

```http
PUT /?abac HTTP/1.1
Host: Bucket.s3.amazonaws.com
Content-MD5: ContentMD5
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-expected-bucket-owner: ExpectedBucketOwner
<?xml version="1.0" encoding="UTF-8"?>
<AbacStatus xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Status>string</Status>
</AbacStatus>
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the general purpose bucket.

Required: Yes

### [Content-MD5](#request-syntax)

The MD5 hash of the `PutBucketAbac` request body.

For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

### [x-amz-expected-bucket-owner](#request-syntax)

The AWS account ID of the general purpose bucket's owner.

### [x-amz-sdk-checksum-algorithm](#request-syntax)

Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see Checking object integrity in the *Amazon S3 User Guide*.

Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body

The request accepts the following data in XML format.

### [AbacStatus](#request-syntax)

Root level tag for the AbacStatus parameters.

Required: Yes

### [Status](#request-syntax)

The ABAC status of the general purpose bucket.

Type: String

Valid Values: `Enabled | Disabled`

Required: No

## Response Syntax

```http
HTTP/1.1 200
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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
