> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_UpdateBucketMetadataInventoryTableConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# UpdateBucketMetadataInventoryTableConfiguration

Enables or disables a live inventory table for an S3 Metadata configuration on a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

## Permissions

To use this operation, you must have the following permissions. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

If you want to encrypt your inventory table with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

- `s3:UpdateBucketMetadataInventoryTableConfiguration`
- `s3tables:CreateTableBucket`
- `s3tables:CreateNamespace`
- `s3tables:GetTable`
- `s3tables:CreateTable`
- `s3tables:PutTablePolicy`
- `s3tables:PutTableEncryption`
- `kms:DescribeKey`

The following operations are related to `UpdateBucketMetadataInventoryTableConfiguration`:

- [CreateBucketMetadataConfiguration](../CreateBucketMetadataConfiguration/CreateBucketMetadataConfiguration.md)
- [DeleteBucketMetadataConfiguration](../DeleteBucketMetadataConfiguration/DeleteBucketMetadataConfiguration.md)
- [GetBucketMetadataConfiguration](../GetBucketMetadataConfiguration/GetBucketMetadataConfiguration.md)
- [UpdateBucketMetadataJournalTableConfiguration](../UpdateBucketMetadataJournalTableConfiguration/UpdateBucketMetadataJournalTableConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
PUT /?metadataInventoryTable HTTP/1.1
Host: Bucket.s3.amazonaws.com
Content-MD5: ContentMD5
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-expected-bucket-owner: ExpectedBucketOwner
<?xml version="1.0" encoding="UTF-8"?>
<InventoryTableConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <ConfigurationState>string</ConfigurationState>
   <EncryptionConfiguration>
      <KmsKeyArn>string</KmsKeyArn>
      <SseAlgorithm>string</SseAlgorithm>
   </EncryptionConfiguration>
</InventoryTableConfiguration>
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that corresponds to the metadata configuration that you want to enable or disable an inventory table for.

Required: Yes

### [Content-MD5](#request-syntax)

The `Content-MD5` header for the inventory table configuration.

### [x-amz-expected-bucket-owner](#request-syntax)

The expected owner of the general purpose bucket that corresponds to the metadata table configuration that you want to enable or disable an inventory table for.

### [x-amz-sdk-checksum-algorithm](#request-syntax)

The checksum algorithm to use with your inventory table configuration.

Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body

The request accepts the following data in XML format.

### [InventoryTableConfiguration](#request-syntax)

Root level tag for the InventoryTableConfiguration parameters.

Required: Yes

### [ConfigurationState](#request-syntax)

The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

### [EncryptionConfiguration](#request-syntax)

The encryption configuration for the inventory table.

Type: MetadataTableEncryptionConfiguration data type

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
