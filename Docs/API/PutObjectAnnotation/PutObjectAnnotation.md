> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_PutObjectAnnotation.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# PutObjectAnnotation

Attaches an annotation to an Amazon S3 object. An annotation is a named payload of 1 byte to 1 MiB that you can associate with a specific object or object version. Each object can have up to 1,000 annotations.

For annotation naming rules and restrictions, see Annotation naming guidelines in the *Amazon S3 User Guide*.

Annotations inherit the encryption of their parent object. For objects without server-side encryption, annotations are encrypted with SSE-S3 (the default for new objects). Objects encrypted with SSE-C cannot have annotations.

To use this operation, you must have the `s3:PutObjectAnnotation` permission. If the bucket has Requester Pays enabled, you must include the `x-amz-request-payer` header.

> **Note**
>
> Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `PutObjectAnnotation`:

- [GetObjectAnnotation](../GetObjectAnnotation/GetObjectAnnotation.md)
- [ListObjectAnnotations](../ListObjectAnnotations/ListObjectAnnotations.md)
- [DeleteObjectAnnotation](../DeleteObjectAnnotation/DeleteObjectAnnotation.md)

## Request Syntax

```http
PUT /{Key+}?annotation&annotationName=AnnotationName&versionId=VersionId HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-object-if-match: ObjectIfMatch
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-checksum-crc32: ChecksumCRC32
x-amz-checksum-crc32c: ChecksumCRC32C
x-amz-checksum-crc64nvme: ChecksumCRC64NVME
x-amz-checksum-sha1: ChecksumSHA1
x-amz-checksum-sha256: ChecksumSHA256
x-amz-checksum-sha512: ChecksumSHA512
x-amz-checksum-md5: ChecksumMD5
x-amz-checksum-xxhash64: ChecksumXXHASH64
x-amz-checksum-xxhash3: ChecksumXXHASH3
x-amz-checksum-xxhash128: ChecksumXXHASH128
Content-MD5: ContentMD5
x-amz-request-payer: RequestPayer
x-amz-expected-bucket-owner: ExpectedBucketOwner

AnnotationPayload
```

## URI Request Parameters

The request uses the following URI parameters.

### [annotationName](#request-syntax)

The name of the annotation.

Length Constraints: Minimum length of 1. Maximum length of 512 bytes.

Required: Yes

### [Bucket](#request-syntax)

The name of the bucket that contains the object.

Required: Yes

### [Content-MD5](#request-syntax)

Base64-encoded MD5 digest of the message.

### [Key](#request-syntax)

The object key.

Length Constraints: Minimum length of 1.

Required: Yes

### [versionId](#request-syntax)

The version ID of the object to attach the annotation to.

### [x-amz-checksum-crc32](#request-syntax)

Base64-encoded CRC32 checksum of the annotation payload.

### [x-amz-checksum-crc32c](#request-syntax)

Base64-encoded CRC32C checksum of the annotation payload.

### [x-amz-checksum-crc64nvme](#request-syntax)

Base64-encoded CRC64NVME checksum of the annotation payload.

### [x-amz-checksum-md5](#request-syntax)

Base64-encoded MD5 checksum of the annotation payload.

### [x-amz-checksum-sha1](#request-syntax)

Base64-encoded SHA1 checksum of the annotation payload.

### [x-amz-checksum-sha256](#request-syntax)

Base64-encoded SHA256 checksum of the annotation payload.

### [x-amz-checksum-sha512](#request-syntax)

Base64-encoded SHA512 checksum of the annotation payload.

### [x-amz-checksum-xxhash128](#request-syntax)

Base64-encoded XXHASH128 checksum of the annotation payload.

### [x-amz-checksum-xxhash3](#request-syntax)

Base64-encoded XXHASH3 checksum of the annotation payload.

### [x-amz-checksum-xxhash64](#request-syntax)

Base64-encoded XXHASH64 checksum of the annotation payload.

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.

### [x-amz-object-if-match](#request-syntax)

If specified, the operation only succeeds if the object's ETag matches the provided value.

### [x-amz-request-payer](#request-syntax)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see Downloading Objects in Requester Pays Buckets in the *Amazon S3 User Guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

### [x-amz-sdk-checksum-algorithm](#request-syntax)

The checksum algorithm to use. Supported values: `CRC32`, `CRC32C`, `CRC64NVME`, `SHA1`, `SHA256`, `SHA512`, `MD5`, `XXHASH64`, `XXHASH3`, `XXHASH128`.

Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body

The request accepts the following binary data.

### [AnnotationPayload](#request-syntax)

## Response Syntax

```http
HTTP/1.1 200
x-amz-object-version-id: ObjectVersionId
ETag: ETag
x-amz-checksum-crc32: ChecksumCRC32
x-amz-checksum-crc32c: ChecksumCRC32C
x-amz-checksum-crc64nvme: ChecksumCRC64NVME
x-amz-checksum-sha1: ChecksumSHA1
x-amz-checksum-sha256: ChecksumSHA256
x-amz-checksum-sha512: ChecksumSHA512
x-amz-checksum-md5: ChecksumMD5
x-amz-checksum-xxhash64: ChecksumXXHASH64
x-amz-checksum-xxhash3: ChecksumXXHASH3
x-amz-checksum-xxhash128: ChecksumXXHASH128
x-amz-checksum-type: ChecksumType
x-amz-server-side-encryption: ServerSideEncryption
x-amz-request-charged: RequestCharged
<?xml version="1.0" encoding="UTF-8"?>
<PutObjectAnnotationOutput>
   <Key>string</Key>
   <AnnotationName>string</AnnotationName>
</PutObjectAnnotationOutput>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

### [ETag](#response-syntax)

The entity tag of the annotation.

### [x-amz-checksum-crc32](#response-syntax)

The CRC32 checksum of the stored annotation.

### [x-amz-checksum-crc32c](#response-syntax)

The CRC32C checksum of the stored annotation.

### [x-amz-checksum-crc64nvme](#response-syntax)

The CRC64NVME checksum of the stored annotation.

### [x-amz-checksum-md5](#response-syntax)

The MD5 checksum of the stored annotation.

### [x-amz-checksum-sha1](#response-syntax)

The SHA1 checksum of the stored annotation.

### [x-amz-checksum-sha256](#response-syntax)

The SHA256 checksum of the stored annotation.

### [x-amz-checksum-sha512](#response-syntax)

The SHA512 checksum of the stored annotation.

### [x-amz-checksum-type](#response-syntax)

The type of checksum used.

Valid Values: `COMPOSITE | FULL_OBJECT`

### [x-amz-checksum-xxhash128](#response-syntax)

The XXHASH128 checksum of the stored annotation.

### [x-amz-checksum-xxhash3](#response-syntax)

The XXHASH3 checksum of the stored annotation.

### [x-amz-checksum-xxhash64](#response-syntax)

The XXHASH64 checksum of the stored annotation.

### [x-amz-object-version-id](#response-syntax)

The version ID of the object that the annotation was attached to.

### [x-amz-request-charged](#response-syntax)

If present, indicates that the requester was successfully charged for the request. For more information, see Using Requester Pays buckets for storage transfers and usage in the *Amazon Simple Storage Service user guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

### [x-amz-server-side-encryption](#response-syntax)

The server-side encryption algorithm used to encrypt the annotation.

Valid Values: `AES256 | aws:fsx | aws:backup | aws:kms | aws:kms:dsse`

The following data is returned in XML format by the service.

### [PutObjectAnnotationOutput](#response-syntax)

Root level tag for the PutObjectAnnotationOutput parameters.

Required: Yes

### [AnnotationName](#response-syntax)

The name of the annotation.

Type: String

### [Key](#response-syntax)

The object key.

Type: String

Length Constraints: Minimum length of 1.

## Errors

### AnnotationLimitExceeded

The request would exceed the maximum number of annotations allowed per object.

HTTP Status Code: 400

### AnnotationNameTooLong

The annotation name exceeds 512 bytes.

HTTP Status Code: 400

### InvalidAnnotationName

The annotation name you provided is invalid.

HTTP Status Code: 400

### InvalidRequest

A parameter or header in your request isn't valid. For details, see the description of this API operation.

HTTP Status Code: 400

### NoSuchBucket

The specified bucket does not exist.

HTTP Status Code: 404

### NoSuchKey

The specified key does not exist.

HTTP Status Code: 404

### UnsupportedMediaType

The annotation payload is not valid UTF-8 encoded text.

HTTP Status Code: 415

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
