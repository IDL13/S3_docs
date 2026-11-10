> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_DeletePublicAccessBlock.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# DeletePublicAccessBlock

> **Note**
>
> This operation is not supported for directory buckets.

Removes the `PublicAccessBlock` configuration for an Amazon S3 bucket. This operation removes the bucket-level configuration only. The effective public access behavior will still be governed by account-level settings (which may inherit from organization-level policies). To use this operation, you must have the `s3:PutBucketPublicAccessBlock` permission. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources.

The following operations are related to `DeletePublicAccessBlock`:

- Using Amazon S3 Block Public Access
- [GetPublicAccessBlock](../GetPublicAccessBlock/GetPublicAccessBlock.md)
- [PutPublicAccessBlock](../PutPublicAccessBlock/PutPublicAccessBlock.md)
- [GetBucketPolicyStatus](../GetBucketPolicyStatus/GetBucketPolicyStatus.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
DELETE /?publicAccessBlock HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The Amazon S3 bucket whose `PublicAccessBlock` configuration you want to delete.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

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
