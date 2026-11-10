> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_ListDirectoryBuckets.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# ListDirectoryBuckets

Returns a list of all Amazon S3 directory buckets owned by the authenticated sender of the request. For more information about directory buckets, see Directory buckets in the *Amazon S3 User Guide*.

> **Note**
>
> **Directory buckets** - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name` . Virtual-hosted-style requests aren't supported. For more information about endpoints in Availability Zones, see Regional and Zonal endpoints for directory buckets in Availability Zones in the *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see Concepts for directory buckets in Local Zones in the *Amazon S3 User Guide*.

## Permissions

You must have the `s3express:ListAllMyDirectoryBuckets` permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource. For more information about directory bucket policies and permissions, see AWS Identity and Access Management (IAM) for S3 Express One Zone in the *Amazon S3 User Guide*.

## HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `s3express-control.region.amazonaws.com`.

> **Note**
>
> The `BucketRegion` response element is not part of the `ListDirectoryBuckets` Response Syntax.

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?continuation-token=ContinuationToken&max-directory-buckets=MaxDirectoryBuckets HTTP/1.1
Host: s3.amazonaws.com
```

## URI Request Parameters

The request uses the following URI parameters.

### [continuation-token](#request-syntax)

`ContinuationToken` indicates to Amazon S3 that the list is being continued on buckets in this account with a token. `ContinuationToken` is obfuscated and is not a real bucket name. You can use this `ContinuationToken` for the pagination of the list results.

Length Constraints: Minimum length of 0. Maximum length of 1024.

### [max-directory-buckets](#request-syntax)

Maximum number of buckets to be returned in response. When the number is more than the count of buckets that are owned by an AWS account, return all the buckets in response.

Valid Range: Minimum value of 0. Maximum value of 1000.

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyDirectoryBucketsResult>
   <Buckets>
      <Bucket>
         <BucketArn>string</BucketArn>
         <BucketRegion>string</BucketRegion>
         <CreationDate>timestamp</CreationDate>
         <Name>string</Name>
      </Bucket>
   </Buckets>
   <ContinuationToken>string</ContinuationToken>
</ListAllMyDirectoryBucketsResult>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [ListAllMyDirectoryBucketsResult](#response-syntax)

Root level tag for the ListAllMyDirectoryBucketsResult parameters.

Required: Yes

### [Buckets](#response-syntax)

The list of buckets owned by the requester.

Type: Array of Bucket data types

### [ContinuationToken](#response-syntax)

If `ContinuationToken` was sent with the request, it is included in the response. You can use the returned `ContinuationToken` for pagination of the list response.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

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
