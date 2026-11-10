> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketRequestPayment.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketRequestPayment

> **Note**
>
> This operation is not supported for directory buckets.

Returns the request payment configuration of a bucket. To use this version of the operation, you must be the bucket owner. For more information, see Requester Pays Buckets.

The following operations are related to `GetBucketRequestPayment`:

- [ListObjects](../ListObjects/ListObjects.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?requestPayment HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the bucket for which to get the payment request configuration

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<RequestPaymentConfiguration>
   <Payer>string</Payer>
</RequestPaymentConfiguration>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [RequestPaymentConfiguration](#response-syntax)

Root level tag for the RequestPaymentConfiguration parameters.

Required: Yes

### [Payer](#response-syntax)

Specifies who pays for the download and request fees.

Type: String

Valid Values: `Requester | BucketOwner`

## Examples

### Sample Request

The following request returns the payer for the bucket, `amzn-s3-demo-bucket`.

```http
            GET ?requestPayment HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 01 Mar 2009 12:00:00 GMT
            Authorization: authorization string
```

### Sample Response

This response shows that the bucket is a Requester Pays bucket, meaning the person requesting a download from this bucket pays the transfer fees.

```http
            HTTP/1.1 200 OK
            x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
            x-amz-request-id: 236A8905248E5A01
            Date: Wed, 01 Mar 2009 12:00:00 GMT
            Content-Type: [type]
            Content-Length: 0
            Connection: close
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <RequestPaymentConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Payer>Requester</Payer>
            </RequestPaymentConfiguration>
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
