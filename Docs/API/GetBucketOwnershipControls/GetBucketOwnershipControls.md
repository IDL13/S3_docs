> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketOwnershipControls.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketOwnershipControls

> **Note**
>
> This operation is not supported for directory buckets.

Retrieves `OwnershipControls` for an Amazon S3 bucket. To use this operation, you must have the `s3:GetBucketOwnershipControls` permission. For more information about Amazon S3 permissions, see Specifying permissions in a policy.

> **Note**
>
> A bucket doesn't have `OwnershipControls` settings in the following cases:
>
> - The bucket was created before the `BucketOwnerEnforced` ownership setting was introduced and you've never explicitly applied this value
> - You've manually deleted the bucket ownership control value using the `DeleteBucketOwnershipControls` API operation.
>
> By default, Amazon S3 sets `OwnershipControls` for all newly created buckets.

For information about Amazon S3 Object Ownership, see Using Object Ownership.

The following operations are related to `GetBucketOwnershipControls`:

- [PutBucketOwnershipControls](../PutBucketOwnershipControls/PutBucketOwnershipControls.md)
- [DeleteBucketOwnershipControls](../DeleteBucketOwnershipControls/DeleteBucketOwnershipControls.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?ownershipControls HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the Amazon S3 bucket whose `OwnershipControls` you want to retrieve.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OwnershipControls>
   <Rule>
      <ObjectOwnership>string</ObjectOwnership>
   </Rule>
   ...
</OwnershipControls>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [OwnershipControls](#response-syntax)

Root level tag for the OwnershipControls parameters.

Required: Yes

### [Rule](#response-syntax)

The container element for an ownership control rule.

Type: Array of OwnershipControlsRule data types

## Examples

### Sample GetBucketOwnershipControls Request for BucketOwnerEnforced

This example illustrates one usage of GetBucketOwnershipControls.

```http
          GET /amzn-s3-demo-bucket?/ownershipControls HTTP/1.1
          Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
          Date: Mon, 29 Nov 2021 00:17:22 GMT
          Authorization: signatureValue;
```

### Sample GetBucketOwnershipControls Response

This example illustrates one usage of GetBucketOwnershipControls.

```http
          HTTP/1.1 200 OK
          x-amz-id-2: Adphn7MaAHDEg9mh5JmcTN8mzyVX0JhIztSiQNaqTxnXXcYi4uiZbYdwWC3JXmh/XXVUUQwO4Vs=
          x-amz-request-id: 252631E05F84A415
          Date: Mon, 29 Nov 2021 00:17:22 GMT
          Server: AmazonS3
          Content-Length: 194

          <OwnershipControls xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Rule>
              <ObjectOwnership>BucketOwnerEnforced</ObjectOwnership>
            </Rule>
          </OwnershipControls>
```

### Sample GetBucketOwnershipControls Request for BucketOwnerPreferred

This example illustrates one usage of GetBucketOwnershipControls.

```http
          GET /amzn-s3-demo-bucket?/ownershipControls HTTP/1.1
          Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
          Date: Thu, 18 Jun 2017 00:17:22 GMT
          Authorization: signatureValue;
```

### Sample GetBucketOwnershipControls Response

This example illustrates one usage of GetBucketOwnershipControls.

```http
          HTTP/1.1 200 OK
          x-amz-id-2: Adphn7MaAHDEg9mh5JmcTN8mzyVX0JhIztSiQNaqTxnXXcYi4uiZbYdwWC3JXmh/XXVUUQwO4Vs=
          x-amz-request-id: 252631E05F84A415
          Date: Thu, 18 Jun 2020 00:17:22 GMT
          Server: AmazonS3
          Content-Length: 194

          <OwnershipControls xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Rule>
              <ObjectOwnership>BucketOwnerPreferred</ObjectOwnership>
            </Rule>
          </OwnershipControls>
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
