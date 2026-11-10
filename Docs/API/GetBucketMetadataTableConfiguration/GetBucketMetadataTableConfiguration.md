> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketMetadataTableConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketMetadataTableConfiguration

> **Important**
>
> We recommend that you retrieve your S3 Metadata configurations by using the V2 [GetBucketMetadataConfiguration](../GetBucketMetadataConfiguration/GetBucketMetadataConfiguration.md) API operation. We no longer recommend using the V1 `GetBucketMetadataTableConfiguration` API operation.
>
> If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](../CreateBucketMetadataConfiguration/CreateBucketMetadataConfiguration.md) so that you can expire journal table records and create a live inventory table.

Retrieves the V1 S3 Metadata configuration for a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

> **Note**
>
> You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 metadata table configurations. However, if you try to use the V1 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you will receive an HTTP `405 Method Not Allowed` error.
>
> Make sure that you update your processes to use the new V2 API operations (`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`, and `DeleteBucketMetadataConfiguration`) instead of the V1 API operations.

## Permissions

To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration` permission. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

The following operations are related to `GetBucketMetadataTableConfiguration`:

- [CreateBucketMetadataTableConfiguration](../CreateBucketMetadataTableConfiguration/CreateBucketMetadataTableConfiguration.md)
- [DeleteBucketMetadataTableConfiguration](../DeleteBucketMetadataTableConfiguration/DeleteBucketMetadataTableConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?metadataTable HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that corresponds to the metadata table configuration that you want to retrieve.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The expected owner of the general purpose bucket that you want to retrieve the metadata table configuration for.

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetBucketMetadataTableConfigurationResult>
   <MetadataTableConfigurationResult>
      <S3TablesDestinationResult>
         <TableArn>string</TableArn>
         <TableBucketArn>string</TableBucketArn>
         <TableName>string</TableName>
         <TableNamespace>string</TableNamespace>
      </S3TablesDestinationResult>
   </MetadataTableConfigurationResult>
   <Status>string</Status>
   <Error>
      <ErrorCode>string</ErrorCode>
      <ErrorMessage>string</ErrorMessage>
   </Error>
</GetBucketMetadataTableConfigurationResult>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [GetBucketMetadataTableConfigurationResult](#response-syntax)

Root level tag for the GetBucketMetadataTableConfigurationResult parameters.

Required: Yes

### [Error](#response-syntax)

If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.

Type: ErrorDetails data type

### [MetadataTableConfigurationResult](#response-syntax)

The V1 S3 Metadata configuration for a general purpose bucket.

Type: MetadataTableConfigurationResult data type

### [Status](#response-syntax)

The status of the metadata table. The status values are:

- `CREATING` - The metadata table is in the process of being created in the specified table bucket.
- `ACTIVE` - The metadata table has been created successfully, and records are being delivered to the table.
- `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver records. See `ErrorDetails` for details.

Type: String

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
