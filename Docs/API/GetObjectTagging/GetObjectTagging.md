> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetObjectTagging.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetObjectTagging

> **Note**
>
> This operation is not supported for directory buckets.

Returns the tag-set of an object. You send the GET request against the tagging subresource associated with the object.

To use this operation, you must have permission to perform the `s3:GetObjectTagging` action. By default, the GET action returns information about current version of an object. For a versioned bucket, you can have multiple versions of an object in your bucket. To retrieve tags of any other version, use the versionId query parameter. You also need permission for the `s3:GetObjectVersionTagging` action.

By default, the bucket owner has this permission and can grant this permission to others.

For information about the Amazon S3 object tagging feature, see Object Tagging.

The following actions are related to `GetObjectTagging`:

- [DeleteObjectTagging](../DeleteObjectTagging/DeleteObjectTagging.md)
- [GetObjectAttributes](../GetObjectAttributes/GetObjectAttributes.md)
- [PutObjectTagging](../PutObjectTagging/PutObjectTagging.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /{Key+}?tagging&versionId=VersionId HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
x-amz-request-payer: RequestPayer
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The bucket name containing the object for which to get the tagging information.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using access points in the *Amazon S3 User Guide*.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `AccessPointName-AccountId.outpostID.s3-outposts.Region.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see What is S3 on Outposts? in the *Amazon S3 User Guide*.

Required: Yes

### [Key](#request-syntax)

Object key for which to get the tagging information.

Length Constraints: Minimum length of 1.

Required: Yes

### [versionId](#request-syntax)

The versionId of the object for which to get the tagging information.

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

### [x-amz-request-payer](#request-syntax)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see Downloading Objects in Requester Pays Buckets in the *Amazon S3 User Guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
x-amz-version-id: VersionId
<?xml version="1.0" encoding="UTF-8"?>
<Tagging>
   <TagSet>
      <Tag>
         <Key>string</Key>
         <Value>string</Value>
      </Tag>
   </TagSet>
</Tagging>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

### [x-amz-version-id](#response-syntax)

The versionId of the object for which you got the tagging information.

The following data is returned in XML format by the service.

### [Tagging](#response-syntax)

Root level tag for the Tagging parameters.

Required: Yes

### [TagSet](#response-syntax)

Contains the tag set.

Type: Array of Tag data types

## Examples

### Sample Request

The following request returns the tag set of the specified object.

```http
            GET /example-object?tagging HTTP/1.1
            Host: examplebucket.s3.<Region>.amazonaws.com
            Date: Thu, 22 Sep 2016 21:33:08 GMT
            Authorization: authorization string
```

### Sample Response

This example illustrates one usage of GetObjectTagging.

```http
            HTTP/1.1 200 OK
            Date: Thu, 22 Sep 2016 21:33:08 GMT
            Connection: close
            Server: AmazonS3
            <?xml version="1.0" encoding="UTF-8"?>
            <Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <TagSet>
                 <Tag>
                   <Key>tag1</Key>
                   <Value>val1</Value>
                </Tag>
                <Tag>
                    <Key>tag2</Key>
                    <Value>val2</Value>
                 </Tag>
              </TagSet>
            </Tagging> 
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
