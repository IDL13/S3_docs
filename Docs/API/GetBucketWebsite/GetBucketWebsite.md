> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketWebsite.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketWebsite

> **Note**
>
> This operation is not supported for directory buckets.

Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a bucket as website by adding a website configuration. For more information about hosting websites, see Hosting Websites on Amazon S3.

This GET action requires the `S3:GetBucketWebsite` permission. By default, only the bucket owner can read the bucket website configuration. However, bucket owners can allow other users to read the website configuration by writing a bucket policy granting them the `S3:GetBucketWebsite` permission.

The following operations are related to `GetBucketWebsite`:

- [DeleteBucketWebsite](../DeleteBucketWebsite/DeleteBucketWebsite.md)
- [PutBucketWebsite](../PutBucketWebsite/PutBucketWebsite.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?website HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The bucket name for which to get the website configuration.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<WebsiteConfiguration>
   <RedirectAllRequestsTo>
      <HostName>string</HostName>
      <Protocol>string</Protocol>
   </RedirectAllRequestsTo>
   <IndexDocument>
      <Suffix>string</Suffix>
   </IndexDocument>
   <ErrorDocument>
      <Key>string</Key>
   </ErrorDocument>
   <RoutingRules>
      <RoutingRule>
         <Condition>
            <HttpErrorCodeReturnedEquals>string</HttpErrorCodeReturnedEquals>
            <KeyPrefixEquals>string</KeyPrefixEquals>
         </Condition>
         <Redirect>
            <HostName>string</HostName>
            <HttpRedirectCode>string</HttpRedirectCode>
            <Protocol>string</Protocol>
            <ReplaceKeyPrefixWith>string</ReplaceKeyPrefixWith>
            <ReplaceKeyWith>string</ReplaceKeyWith>
         </Redirect>
      </RoutingRule>
   </RoutingRules>
</WebsiteConfiguration>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [WebsiteConfiguration](#response-syntax)

Root level tag for the WebsiteConfiguration parameters.

Required: Yes

### [ErrorDocument](#response-syntax)

The object key name of the website error document to use for 4XX class errors.

Type: ErrorDocument data type

### [IndexDocument](#response-syntax)

The name of the index document for the website (for example `index.html`).

Type: IndexDocument data type

### [RedirectAllRequestsTo](#response-syntax)

Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

Type: RedirectAllRequestsTo data type

### [RoutingRules](#response-syntax)

Rules that define when a redirect is applied and the redirect behavior.

Type: Array of RoutingRule data types

## Examples

### Sample Request

This request retrieves website configuration on the specified bucket.

```http
            GET ?website HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Thu, 27 Jan 2011 00:49:20 GMT
            Authorization: AWS AKIAIOSFODNN7EXAMPLE:n0Nhek72Ufg/u7Sm5C1dqRLs8XX=
```

### Sample Response

This example illustrates one usage of GetBucketWebsite.

```http
         HTTP/1.1 200 OK
         x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
         x-amz-request-id: 3848CD259D811111
         Date: Thu, 27 Jan 2011 00:49:26 GMT
         Content-Length: 240
         Content-Type: application/xml
         Transfer-Encoding: chunked
         Server: AmazonS3

         <?xml version="1.0" encoding="UTF-8"?>
         <WebsiteConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
           <IndexDocument>
             <Suffix>index.html</Suffix>
           </IndexDocument>
          <ErrorDocument>
            <Key>404.html</Key>
          </ErrorDocument>
         </WebsiteConfiguration>
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
