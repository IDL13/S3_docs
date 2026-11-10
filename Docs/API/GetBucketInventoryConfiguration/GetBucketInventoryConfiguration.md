> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_GetBucketInventoryConfiguration.html`. Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, ссылки на материалы вне справочника оставлены обычным текстом.

# GetBucketInventoryConfiguration

Returns an S3 Inventory configuration (identified by the inventory configuration ID) from the bucket.

> **Note**
>
> **Directory buckets** - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name` . Virtual-hosted-style requests aren't supported. For more information about endpoints in Availability Zones, see Regional and Zonal endpoints for directory buckets in Availability Zones in the *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see Concepts for directory buckets in Local Zones in the *Amazon S3 User Guide*.

## Permissions

To use this operation, you must have permissions to perform the `s3:GetInventoryConfiguration` action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources.

- **General purpose bucket permissions** - The `s3:GetInventoryConfiguration` permission is required in a policy. For more information about general purpose buckets permissions, see Using Bucket Policies and User Policies in the *Amazon S3 User Guide*.
- **Directory bucket permissions** - To grant access to this API operation, you must have the `s3express:GetInventoryConfiguration` permission in an IAM identity-based policy instead of a bucket policy. For more information about directory bucket policies and permissions, see AWS Identity and Access Management (IAM) for S3 Express One Zone in the *Amazon S3 User Guide*.

## HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

For information about the Amazon S3 inventory feature, see Amazon S3 Inventory.

The following operations are related to `GetBucketInventoryConfiguration`:

- [DeleteBucketInventoryConfiguration](../DeleteBucketInventoryConfiguration/DeleteBucketInventoryConfiguration.md)
- [ListBucketInventoryConfigurations](../ListBucketInventoryConfigurations/ListBucketInventoryConfigurations.md)
- [PutBucketInventoryConfiguration](../PutBucketInventoryConfiguration/PutBucketInventoryConfiguration.md)

> **Important**
>
> You must URL encode any signed header values that contain spaces. For example, if your header value is `my  file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax

```http
GET /?inventory&id=Id HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-expected-bucket-owner: ExpectedBucketOwner
```

## URI Request Parameters

The request uses the following URI parameters.

### [Bucket](#request-syntax)

The name of the bucket containing the inventory configuration to retrieve.

**Directory buckets** - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name` . Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `bucket-base-name--zone-id--x-s3` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see Directory bucket naming rules in the *Amazon S3 User Guide*

Required: Yes

### [id](#request-syntax)

The ID used to identify the inventory configuration.

Required: Yes

### [x-amz-expected-bucket-owner](#request-syntax)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

> **Note**
>
> For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code `501 Not Implemented`.

## Request Body

The request does not have a request body.

## Response Syntax

```http
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<InventoryConfiguration>
   <Destination>
      <S3BucketDestination>
         <AccountId>string</AccountId>
         <Bucket>string</Bucket>
         <Encryption>
            <SSE-KMS>
               <KeyId>string</KeyId>
            </SSE-KMS>
            <SSE-S3>
            </SSE-S3>
         </Encryption>
         <Format>string</Format>
         <Prefix>string</Prefix>
      </S3BucketDestination>
   </Destination>
   <IsEnabled>boolean</IsEnabled>
   <Filter>
      <Prefix>string</Prefix>
   </Filter>
   <Id>string</Id>
   <IncludedObjectVersions>string</IncludedObjectVersions>
   <OptionalFields>
      <Field>string</Field>
   </OptionalFields>
   <Schedule>
      <Frequency>string</Frequency>
   </Schedule>
</InventoryConfiguration>
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

### [InventoryConfiguration](#response-syntax)

Root level tag for the InventoryConfiguration parameters.

Required: Yes

### [Destination](#response-syntax)

Contains information about where to publish the inventory results.

Type: InventoryDestination data type

### [Filter](#response-syntax)

Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.

Type: InventoryFilter data type

### [Id](#response-syntax)

The ID used to identify the inventory configuration.

Type: String

### [IncludedObjectVersions](#response-syntax)

Object versions to include in the inventory list. If set to `All`, the list includes all the object versions, which adds the version-related fields `VersionId`, `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the list does not contain these version-related fields.

Type: String

Valid Values: `All | Current`

### [IsEnabled](#response-syntax)

Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory list is generated. If set to `False`, no inventory list is generated.

Type: Boolean

### [OptionalFields](#response-syntax)

Contains the optional fields that are included in the inventory results.

> **Note**
>
> The following optional fields are supported for directory buckets `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate.` Throws MalformedXML error if unsupported optional field is provided.

Type: Array of strings

Valid Values: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus | ObjectLockRetainUntilDate | ObjectLockMode | ObjectLockLegalHoldStatus | ObjectLockEventHoldStatus | ObjectLockEventHoldDuration | IntelligentTieringAccessTier | BucketKeyStatus | ChecksumAlgorithm | ObjectAccessControlList | ObjectOwner | LifecycleExpirationDate`

### [Schedule](#response-syntax)

Specifies the schedule for generating inventory results.

Type: InventorySchedule data type

## Examples

### Sample Request: Configure an inventory report

The following GET request for the bucket `examplebucket` returns the inventory configuration with the ID `list1`.

```http
            GET /?inventory&id=list1 HTTP/1.1
            Host: examplebucket.s3.<Region>.amazonaws.com
            Date: Mon, 31 Oct 2016 12:00:00 GMT
            Authorization: authorization string 
```

### Sample Response

This example illustrates one usage of GetBucketInventoryConfiguration.

```http
         HTTP/1.1 200 OK
         x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
         x-amz-request-id: 236A8905248E5A02
         Date: Mon, 31 Oct 2016 12:00:00 GMT
         Server: AmazonS3
         Content-Length: length

         <?xml version="1.0" encoding="UTF-8"?>
         <InventoryConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Id>report1</Id>
           <IsEnabled>true</IsEnabled>
           <Destination>
              <S3BucketDestination>
                 <Format>CSV</Format>
                  <AccountId>123456789012</AccountId>
                  <Bucket>arn:aws:s3:::destination-bucket</Bucket>
                 <Prefix>prefix1</Prefix>
                 <SSE-S3/>
               </S3BucketDestination>
            </Destination>
            <Schedule>
               <Frequency>Daily</Frequency>
           </Schedule>
           <Filter>
             <Prefix>myprefix/</Prefix>
           </Filter>
           <IncludedObjectVersions>All</IncludedObjectVersions>
           <OptionalFields>
             <Field>Size</Field>
             <Field>LastModifiedDate</Field>
               <Field>ETag</Field>
               <Field>StorageClass</Field>
               <Field>IsMultipartUploaded</Field>
             <Field>ReplicationStatus</Field>
               <Field>ObjectLockRetainUntilDate</Field>
               <Field>ObjectLockMode</Field>
             <Field>ObjectLockLegalHoldStatus</Field> 
          </OptionalFields>
         </InventoryConfiguration>
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
