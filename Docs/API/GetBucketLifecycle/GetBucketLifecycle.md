> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketLifecycle.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketLifecycle

> **Important**
>
> For an updated version of this API, see [GetBucketLifecycleConfiguration](../GetBucketLifecycleConfiguration/GetBucketLifecycleConfiguration.md). If you configured a bucket lifecycle using the `filter` element, you should see the updated version of this topic. This topic is provided for backward compatibility.

> **Note**
>
> This operation is not supported for directory buckets.

Returns the lifecycle configuration information set on the bucket. For information about lifecycle configuration, see Object Lifecycle Management.

To use this operation, you must have permission to perform the `s3:GetLifecycleConfiguration` action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources.

`GetBucketLifecycle` has the following special error:

- Error code: `NoSuchLifecycleConfiguration`

  - Description: The lifecycle configuration does not exist.
  - HTTP Status Code: 404 Not Found
  - SOAP Fault Code Prefix: Client

The following operations are related to `GetBucketLifecycle`:

- [GetBucketLifecycleConfiguration](../GetBucketLifecycleConfiguration/GetBucketLifecycleConfiguration.md)
- [PutBucketLifecycle](../PutBucketLifecycle/PutBucketLifecycle.md)
- [DeleteBucketLifecycle](../DeleteBucketLifecycle/DeleteBucketLifecycle.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?lifecycle HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the bucket for which to get the lifecycle information.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
   <Rule>
      <AbortIncompleteMultipartUpload>
         <DaysAfterInitiation>integer</DaysAfterInitiation>
      </AbortIncompleteMultipartUpload>
      <Expiration>
         <Date>timestamp</Date>
         <Days>integer</Days>
         <ExpiredObjectDeleteMarker>boolean</ExpiredObjectDeleteMarker>
      </Expiration>
      <ID>string</ID>
      <NoncurrentVersionExpiration>
         <NewerNoncurrentVersions>integer</NewerNoncurrentVersions>
         <NoncurrentDays>integer</NoncurrentDays>
      </NoncurrentVersionExpiration>
      <NoncurrentVersionTransition>
         <NewerNoncurrentVersions>integer</NewerNoncurrentVersions>
         <NoncurrentDays>integer</NoncurrentDays>
         <StorageClass>string</StorageClass>
      </NoncurrentVersionTransition>
      <Prefix>string</Prefix>
      <Status>string</Status>
      <Transition>
         <Date>timestamp</Date>
         <Days>integer</Days>
         <StorageClass>string</StorageClass>
      </Transition>
   </Rule>
   ...
</LifecycleConfiguration>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [LifecycleConfiguration](#response-syntax)

Root level tag for the LifecycleConfiguration parameters.

Required: Yes

### [Rule](#response-syntax)

Container for a lifecycle rule.

Type: Array of Rule data types

## Examples

### Sample Request: Retrieve a lifecycle subresource

This example is a GET request to retrieve the lifecycle subresource from the specified bucket, and an example response with the returned lifecycle configuration.

```http
            GET /?lifecycle HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
            Authorization: signatureValue
```

### Sample Response

This example illustrates one usage of GetBucketLifecycle.

```http
            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4RyTmXa3rPi4hklTXouTf0hccUjo0iCPjz6FnfIutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991C342C575321
            Date: Thu, 15 Nov 2012 00:17:23 GMT
            Server: AmazonS3
            Content-Length: 358

            <?xml version="1.0" encoding="UTF-8"?>
            <LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Rule>
                    <ID>Archive and then delete rule</ID>
                    <Prefix>projectdocs/</Prefix>
                   <Status>Enabled</Status>
                  <Transition>
                       <Days>30</Days>
                       <StorageClass>STANDARD_IA</StorageClass>
                  </Transition>
                  <Transition>
                     <Days>365</Days>
                      <StorageClass>GLACIER</StorageClass>
                   </Transition>
                   <Expiration>
                      <Days>3650</Days>
                   </Expiration>
               </Rule>
            </LifecycleConfiguration>
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
