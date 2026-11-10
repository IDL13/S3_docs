> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketMetadataConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketMetadataConfiguration

Retrieves the S3 Metadata configuration for a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

> **Note**
>
> You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 metadata configurations. However, if you try to use the V1 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you will receive an HTTP `405 Method Not Allowed` error.

## Permissions

To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration` permission. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

> **Note**
>
> The IAM policy action name is the same for the V1 and V2 API operations.

The following operations are related to `GetBucketMetadataConfiguration`:

- [CreateBucketMetadataConfiguration](../CreateBucketMetadataConfiguration/CreateBucketMetadataConfiguration.md)
- [DeleteBucketMetadataConfiguration](../DeleteBucketMetadataConfiguration/DeleteBucketMetadataConfiguration.md)
- [UpdateBucketMetadataInventoryTableConfiguration](../UpdateBucketMetadataInventoryTableConfiguration/UpdateBucketMetadataInventoryTableConfiguration.md)
- [UpdateBucketMetadataJournalTableConfiguration](../UpdateBucketMetadataJournalTableConfiguration/UpdateBucketMetadataJournalTableConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?metadataConfiguration HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that corresponds to the metadata configuration that you want to retrieve.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The expected owner of the general purpose bucket that you want to retrieve the metadata table configuration for.

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetBucketMetadataConfigurationResult>
   <MetadataConfigurationResult>
      <AnnotationTableConfigurationResult>
         <ConfigurationState>string</ConfigurationState>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <Role>string</Role>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </AnnotationTableConfigurationResult>
      <DestinationResult>
         <TableBucketArn>string</TableBucketArn>
         <TableBucketType>string</TableBucketType>
         <TableNamespace>string</TableNamespace>
      </DestinationResult>
      <InventoryTableConfigurationResult>
         <ConfigurationState>string</ConfigurationState>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </InventoryTableConfigurationResult>
      <JournalTableConfigurationResult>
         <Error>
            <ErrorCode>string</ErrorCode>
            <ErrorMessage>string</ErrorMessage>
         </Error>
         <RecordExpiration>
            <Days>integer</Days>
            <Expiration>string</Expiration>
         </RecordExpiration>
         <TableArn>string</TableArn>
         <TableName>string</TableName>
         <TableStatus>string</TableStatus>
      </JournalTableConfigurationResult>
   </MetadataConfigurationResult>
</GetBucketMetadataConfigurationResult>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [GetBucketMetadataConfigurationResult](#response-syntax)

Root level tag for the GetBucketMetadataConfigurationResult parameters.

Required: Yes

### [MetadataConfigurationResult](#response-syntax)

The metadata configuration for a general purpose bucket.

Type: MetadataConfigurationResult data type

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
