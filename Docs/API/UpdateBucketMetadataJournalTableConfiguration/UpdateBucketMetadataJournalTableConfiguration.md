> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_UpdateBucketMetadataJournalTableConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# UpdateBucketMetadataJournalTableConfiguration

Enables or disables journal table record expiration for an S3 Metadata configuration on a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

## Permissions

To use this operation, you must have the `s3:UpdateBucketMetadataJournalTableConfiguration` permission. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

The following operations are related to `UpdateBucketMetadataJournalTableConfiguration`:

- [CreateBucketMetadataConfiguration](../CreateBucketMetadataConfiguration/CreateBucketMetadataConfiguration.md)
- [DeleteBucketMetadataConfiguration](../DeleteBucketMetadataConfiguration/DeleteBucketMetadataConfiguration.md)
- [GetBucketMetadataConfiguration](../GetBucketMetadataConfiguration/GetBucketMetadataConfiguration.md)
- [UpdateBucketMetadataInventoryTableConfiguration](../UpdateBucketMetadataInventoryTableConfiguration/UpdateBucketMetadataInventoryTableConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
PUT /?metadataJournalTable HTTP/1.1
Host: Bucket.s3.amazonaws.com
Content-MD5: ContentMD5
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-expected-bucket-owner: ExpectedBucketOwner
<?xml version="1.0" encoding="UTF-8"?>
<JournalTableConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <RecordExpiration>
      <Days>integer</Days>
      <Expiration>string</Expiration>
   </RecordExpiration>
</JournalTableConfiguration>
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that corresponds to the metadata configuration that you want to enable or disable journal table record expiration for.

Required: Yes

### [Content-MD5](#request-syntax)

The `Content-MD5` header for the journal table configuration.

### [x-amz-expected-bucket-owner](#request-syntax)

The expected owner of the general purpose bucket that corresponds to the metadata table configuration that you want to enable or disable journal table record expiration for.

### [x-amz-sdk-checksum-algorithm](#request-syntax)

The checksum algorithm to use with your journal table configuration.

Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body

The request accepts the following data in XML format.

### [JournalTableConfiguration](#request-syntax)

Root level tag for the JournalTableConfiguration parameters.

Required: Yes

### [RecordExpiration](#request-syntax)

The journal table record expiration settings for the journal table.

Type: RecordExpiration data type

Required: Yes

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
