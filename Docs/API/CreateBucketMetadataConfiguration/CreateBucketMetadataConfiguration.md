> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_CreateBucketMetadataConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# CreateBucketMetadataConfiguration

Creates an S3 Metadata V2 metadata configuration for a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

## Permissions

To use this operation, you must have the following permissions. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

If you also want to integrate your table bucket with AWS analytics services so that you can query your metadata table, you need additional permissions. For more information, see Integrating Amazon S3 Tables with AWS analytics services in the *Amazon S3 User Guide*.

To query your metadata tables, you need additional permissions. For more information, see Permissions for querying metadata tables in the *Amazon S3 User Guide*.

- `s3:CreateBucketMetadataTableConfiguration`

  > **Note**
  >
  > The IAM policy action name is the same for the V1 and V2 API operations.
- `s3tables:CreateTableBucket`
- `s3tables:CreateNamespace`
- `s3tables:GetTable`
- `s3tables:CreateTable`
- `s3tables:PutTablePolicy`
- `s3tables:PutTableBucketPolicy`
- `s3tables:PutTableEncryption`
- `kms:DescribeKey`
- `iam:PassRole` - required if you include an `AnnotationTableConfiguration` with an IAM role.

The following operations are related to `CreateBucketMetadataConfiguration`:

- [DeleteBucketMetadataConfiguration](../DeleteBucketMetadataConfiguration/DeleteBucketMetadataConfiguration.md)
- [GetBucketMetadataConfiguration](../GetBucketMetadataConfiguration/GetBucketMetadataConfiguration.md)
- [UpdateBucketMetadataInventoryTableConfiguration](../UpdateBucketMetadataInventoryTableConfiguration/UpdateBucketMetadataInventoryTableConfiguration.md)
- [UpdateBucketMetadataJournalTableConfiguration](../UpdateBucketMetadataJournalTableConfiguration/UpdateBucketMetadataJournalTableConfiguration.md)
- [UpdateBucketMetadataAnnotationTableConfiguration](../UpdateBucketMetadataAnnotationTableConfiguration/UpdateBucketMetadataAnnotationTableConfiguration.md)

If you include an `AnnotationTableConfiguration` with an IAM role, the role must have a trust policy that allows the Amazon S3 metadata service to assume it, and a permissions policy that grants the actions needed to read annotations from your bucket. The following examples show a trust policy and a permissions policy that you can adapt for your bucket and account.

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
POST /?metadataConfiguration HTTP/1.1
Host: Bucket.s3.amazonaws.com
Content-MD5: ContentMD5
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-expected-bucket-owner: ExpectedBucketOwner
<?xml version="1.0" encoding="UTF-8"?>
<MetadataConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <JournalTableConfiguration>
      <EncryptionConfiguration>
         <KmsKeyArn>string</KmsKeyArn>
         <SseAlgorithm>string</SseAlgorithm>
      </EncryptionConfiguration>
      <RecordExpiration>
         <Days>integer</Days>
         <Expiration>string</Expiration>
      </RecordExpiration>
   </JournalTableConfiguration>
   <InventoryTableConfiguration>
      <ConfigurationState>string</ConfigurationState>
      <EncryptionConfiguration>
         <KmsKeyArn>string</KmsKeyArn>
         <SseAlgorithm>string</SseAlgorithm>
      </EncryptionConfiguration>
   </InventoryTableConfiguration>
   <AnnotationTableConfiguration>
      <ConfigurationState>string</ConfigurationState>
      <EncryptionConfiguration>
         <KmsKeyArn>string</KmsKeyArn>
         <SseAlgorithm>string</SseAlgorithm>
      </EncryptionConfiguration>
      <Role>string</Role>
   </AnnotationTableConfiguration>
</MetadataConfiguration>
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that you want to create the metadata configuration for.

Required: Yes

### [Content-MD5](#request-syntax)

The `Content-MD5` header for the metadata configuration.

### [x-amz-expected-bucket-owner](#request-syntax)

The expected owner of the general purpose bucket that corresponds to your metadata configuration.

### [x-amz-sdk-checksum-algorithm](#request-syntax)

The checksum algorithm to use with your metadata configuration.

Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body

The request accepts the following data in XML format.

### [MetadataConfiguration](#request-syntax)

Root level tag for the MetadataConfiguration parameters.

Required: Yes

### [AnnotationTableConfiguration](#request-syntax)

Optional annotation table configuration to include with the metadata configuration.

Type: AnnotationTableConfiguration data type

Required: No

### [InventoryTableConfiguration](#request-syntax)

The inventory table configuration for a metadata configuration.

Type: InventoryTableConfiguration data type

Required: No

### [JournalTableConfiguration](#request-syntax)

The journal table configuration for a metadata configuration.

Type: JournalTableConfiguration data type

Required: Yes

## Response Syntax

```http
HTTP/1.1 200
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples

### Trust policy

This example illustrates one usage of CreateBucketMetadataConfiguration.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "metadata.s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
                }
            }
        }
    ]
}
```

### Permissions policy

This example illustrates one usage of CreateBucketMetadataConfiguration.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PermissionForGetAnnotation",
      "Effect": "Allow",
      "Action": [
        "s3:GetObjectAnnotation",
        "s3:GetObjectVersionAnnotation"
      ],
      "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket/*"],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "PermissionsForListBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:ListBucketVersions"
      ],
      "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket"],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "PermissionsForDecryptAnnotation",
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Condition": {
        "StringLike": {
          "kms:ViaService": [
            "s3.us-east-1.amazonaws.com"
          ]
        },
        "ArnLike": {
          "kms:EncryptionContext:aws:s3:arn": [
            "arn:aws:s3:::amzn-s3-demo-bucket",
            "arn:aws:s3:::amzn-s3-demo-bucket/*"
          ]
        }
      },
      "Resource": ["*"]
    }
  ]
}
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
