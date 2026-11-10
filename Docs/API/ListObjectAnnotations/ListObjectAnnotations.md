> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_ListObjectAnnotations.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# ListObjectAnnotations

Lists the annotations attached to an Amazon S3 object. Results are paginated, with a maximum of 1,000 annotations per object. Use the `AnnotationPrefix` parameter to filter the results by name prefix.

To use this operation, you must have the `s3:ListObjectAnnotations` permission.

> **Note**
>
> Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, and S3 Express One Zone (directory buckets).

The following operations are related to `ListObjectAnnotations`:

- [PutObjectAnnotation](../PutObjectAnnotation/PutObjectAnnotation.md)
- [GetObjectAnnotation](../GetObjectAnnotation/GetObjectAnnotation.md)
- [DeleteObjectAnnotation](../DeleteObjectAnnotation/DeleteObjectAnnotation.md)

## Request Syntax

```http
GET /{Key+}?annotation&annotation-prefix=AnnotationPrefix&continuation-token=ContinuationToken&max-annotation-results=MaxAnnotationResults&versionId=VersionId HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-request-payer: RequestPayer
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [annotation-prefix](#request-syntax)

Filter results to annotations whose name begins with the specified prefix.

### [Bucket](#request-syntax)

The name of the bucket that contains the object.

Required: Yes

### [continuation-token](#request-syntax)

Continuation token returned by a previous request to retrieve the next page.

### [Key](#request-syntax)

The object key.

Length Constraints: Minimum length of 1.

Required: Yes

### [max-annotation-results](#request-syntax)

The maximum number of annotations to return in the response. Maximum is 1,000.

Valid Range: Minimum value of 1. Maximum value of 1000.

### [versionId](#request-syntax)

The version ID of the object.

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner.

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
x-amz-object-version-id: ObjectVersionId
x-amz-request-charged: RequestCharged
<?xml version="1.0" encoding="UTF-8"?>
<ListObjectAnnotationsOutput>
   <Annotations>
      <AnnotationEntry>
         <AnnotationName>string</AnnotationName>
         <ChecksumAlgorithm>string</ChecksumAlgorithm>
         ...
         <ETag>string</ETag>
         <LastModified>timestamp</LastModified>
         <ReplicationStatus>string</ReplicationStatus>
         <Size>long</Size>
      </AnnotationEntry>
   </Annotations>
   <Bucket>string</Bucket>
   <Key>string</Key>
   <AnnotationPrefix>string</AnnotationPrefix>
   <MaxAnnotationResults>integer</MaxAnnotationResults>
   <AnnotationCount>integer</AnnotationCount>
   <ContinuationToken>string</ContinuationToken>
   <NextContinuationToken>string</NextContinuationToken>
</ListObjectAnnotationsOutput>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

### [x-amz-object-version-id](#response-syntax)

The version ID of the object.

### [x-amz-request-charged](#response-syntax)

If present, indicates that the requester was successfully charged for the request. For more information, see Using Requester Pays buckets for storage transfers and usage in the *Amazon Simple Storage Service user guide*.

> **Note**
>
> This functionality is not supported for directory buckets.

Valid Values: `requester`

The following data is returned in XML format by the service.

### [ListObjectAnnotationsOutput](#response-syntax)

Root level tag for the ListObjectAnnotationsOutput parameters.

Required: Yes

### [AnnotationCount](#response-syntax)

The number of annotations returned.

Type: Integer

### [AnnotationPrefix](#response-syntax)

The prefix used to filter the response.

Type: String

### [Annotations](#response-syntax)

The list of annotations attached to the object.

Type: Array of AnnotationEntry data types

### [Bucket](#response-syntax)

The bucket name.

Type: String

### [ContinuationToken](#response-syntax)

The continuation token used in this request.

Type: String

### [Key](#response-syntax)

The object key.

Type: String

Length Constraints: Minimum length of 1.

### [MaxAnnotationResults](#response-syntax)

The maximum number of annotations returned in the response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 1000.

### [NextContinuationToken](#response-syntax)

The continuation token to use to retrieve the next page of results.

Type: String

## Errors

### InvalidPrefix

The annotation prefix you provided is invalid.

HTTP Status Code: 400

### NoSuchBucket

The specified bucket does not exist.

HTTP Status Code: 404

### NoSuchKey

The specified key does not exist.

HTTP Status Code: 404

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
