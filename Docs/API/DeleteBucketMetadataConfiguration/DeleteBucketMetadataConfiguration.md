> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_DeleteBucketMetadataConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# DeleteBucketMetadataConfiguration

Deletes an S3 Metadata configuration from a general purpose bucket. For more information, see Accelerating data discovery with S3 Metadata in the *Amazon S3 User Guide*.

> **Note**
>
> You can use the V2 `DeleteBucketMetadataConfiguration` API operation with V1 or V2 metadata configurations. However, if you try to use the V1 `DeleteBucketMetadataTableConfiguration` API operation with V2 configurations, you will receive an HTTP `405 Method Not Allowed` error.

## Permissions

To use this operation, you must have the `s3:DeleteBucketMetadataTableConfiguration` permission. For more information, see Setting up permissions for configuring metadata tables in the *Amazon S3 User Guide*.

> **Note**
>
> The IAM policy action name is the same for the V1 and V2 API operations.

The following operations are related to `DeleteBucketMetadataConfiguration`:

- [CreateBucketMetadataConfiguration](../CreateBucketMetadataConfiguration/CreateBucketMetadataConfiguration.md)
- [GetBucketMetadataConfiguration](../GetBucketMetadataConfiguration/GetBucketMetadataConfiguration.md)
- [UpdateBucketMetadataInventoryTableConfiguration](../UpdateBucketMetadataInventoryTableConfiguration/UpdateBucketMetadataInventoryTableConfiguration.md)
- [UpdateBucketMetadataJournalTableConfiguration](../UpdateBucketMetadataJournalTableConfiguration/UpdateBucketMetadataJournalTableConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
DELETE /?metadataConfiguration HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The general purpose bucket that you want to remove the metadata configuration from.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The expected bucket owner of the general purpose bucket that you want to remove the metadata table configuration from.

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 204
```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

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
