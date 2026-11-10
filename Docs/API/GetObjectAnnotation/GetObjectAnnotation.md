> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetObjectAnnotation.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetObjectAnnotation

Retrieves an annotation from an Amazon S3 object. To use this operation, you must have the `s3:GetObjectAnnotation` permission.

If checksum mode is enabled via the `x-amz-checksum-mode` header, Amazon S3 returns the stored checksum in the response headers for client-side validation.

> **Note**
>
> Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `GetObjectAnnotation`:

- [PutObjectAnnotation](../PutObjectAnnotation/PutObjectAnnotation.md)
- [ListObjectAnnotations](../ListObjectAnnotations/ListObjectAnnotations.md)
- [DeleteObjectAnnotation](../DeleteObjectAnnotation/DeleteObjectAnnotation.md)

## Request Syntax

```http
GET /{Key+}?annotation&annotationName=AnnotationName&versionId=VersionId HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-request-payer: RequestPayer
x-amz-expected-bucket-owner: ExpectedBucketOwner
x-amz-checksum-mode: ChecksumMode
```

## URI Request Parameters

The request uses the following URI parameters.

### [annotationName](#request-syntax)

The name of the annotation to retrieve.

Length Constraints: Minimum length of 1. Maximum length of 512 bytes.

Required: Yes

### [Bucket](#request-syntax)

The name of the bucket that contains the object.

Required: Yes

### [Key](#request-syntax)

The object key.

Length Constraints: Minimum length of 1.

Required: Yes

### [versionId](#request-syntax)

The version ID of the object.

### [x-amz-checksum-mode](#request-syntax)

Set to `ENABLED` to validate the checksum of the annotation payload on retrieval.

Valid Values: `ENABLED`

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.

### [x-amz-request-payer](#request-syntax)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see Downloading Objects in Requester Pays Buckets in the *Amazon S3 User Guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
x-amz-object-version-id: ObjectVersionId
Last-Modified: LastModified
Content-Length: ContentLength
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
x-amz-replication-status: ReplicationStatus

AnnotationPayload
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

### [Content-Length](#response-syntax)

The size of the annotation payload, in bytes.

### [ETag](#response-syntax)

The entity tag of the annotation.

### [Last-Modified](#response-syntax)

The date and time the annotation was last modified.

### [x-amz-checksum-crc32](#response-syntax)

The CRC32 checksum of the annotation payload.

### [x-amz-checksum-crc32c](#response-syntax)

The CRC32C checksum of the annotation payload.

### [x-amz-checksum-crc64nvme](#response-syntax)

The CRC64NVME checksum of the annotation payload.

### [x-amz-checksum-md5](#response-syntax)

The MD5 checksum of the annotation payload.

### [x-amz-checksum-sha1](#response-syntax)

The SHA1 checksum of the annotation payload.

### [x-amz-checksum-sha256](#response-syntax)

The SHA256 checksum of the annotation payload.

### [x-amz-checksum-sha512](#response-syntax)

The SHA512 checksum of the annotation payload.

### [x-amz-checksum-type](#response-syntax)

The type of checksum used.

Valid Values: `COMPOSITE | FULL_OBJECT`

### [x-amz-checksum-xxhash128](#response-syntax)

The XXHASH128 checksum of the annotation payload.

### [x-amz-checksum-xxhash3](#response-syntax)

The XXHASH3 checksum of the annotation payload.

### [x-amz-checksum-xxhash64](#response-syntax)

The XXHASH64 checksum of the annotation payload.

### [x-amz-object-version-id](#response-syntax)

The version ID of the object that the annotation is attached to.

### [x-amz-replication-status](#response-syntax)

The replication status of the annotation. Possible values include `PENDING`, `COMPLETED`, `FAILED`, and `REPLICA`.

Valid Values: `COMPLETE | PENDING | FAILED | REPLICA | COMPLETED`

### [x-amz-request-charged](#response-syntax)

If present, indicates that the requester was successfully charged for the request. For more information, see Using Requester Pays buckets for storage transfers and usage in the *Amazon Simple Storage Service user guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

### [x-amz-server-side-encryption](#response-syntax)

The server-side encryption algorithm used.

Valid Values: `AES256 | aws:fsx | aws:backup | aws:kms | aws:kms:dsse`

The following data is returned in binary format by the service.

### [AnnotationPayload](#response-syntax)

## Errors

### NoSuchAnnotation

The specified annotation does not exist on this object.

HTTP Status Code: 404

### NoSuchBucket

The specified bucket does not exist.

HTTP Status Code: 404

### NoSuchKey

The specified key does not exist.

HTTP Status Code: 404

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
