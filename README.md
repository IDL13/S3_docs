# S3 Docs

Офлайн-справочник по 116 операциям из раздела **Amazon S3** в Amazon S3 API Reference. Разделы Amazon S3 Control, Files, Outposts, Tables и Vectors имеют собственные списки операций.

## Как работать со справочником

1. Найди точное имя операции в оглавлении. У схожих операций, например `ListObjects` и `ListObjectsV2`, отдельные папки.
2. Открой `Docs/API/<Operation>/README.md` и статью `<Operation>.md` в той же папке. В README описано, что проверить. Статья содержит полный английский текст в Markdown с параметрами, примечаниями и блоками HTTP/XML.
3. Переходи к связанным операциям по локальным ссылкам. Используй схемы запроса и ответа, описание разрешений и ошибок из скопированных статей. Если статья отсылает к материалу вне справочника, используй доступные здесь сведения и явно обозначай пробел.
4. При ответе разделяй контракт AWS, наблюдаемое поведение и проектные решения для совместимой реализации. Ссылайся на локальный файл и раздел статьи.

## Обновление копии для сопровождающего

Для запуска нужен Python 3.8+. Скрипты используют стандартную библиотеку, поэтому установку из `requirements.txt` можно пропустить. Чтобы использовать другой интерпретатор, передай `PYTHON=/путь/к/python3` в команду `make`.

| Команда | Действие |
| --- | --- |
| `make check` | Проверяет заголовки операций, блоки кода и отсутствие сырого HTML в локальных статьях без записи файлов. |
| `make convert` | Преобразует прежние HTML-снимки в Markdown без сети. Готовые Markdown-статьи проверяет и пропускает. |
| `make import` | Скачивает статьи с `docs.aws.amazon.com` и сохраняет их в Markdown. Требуется доступ к AWS. |
| `make install` | Устанавливает зависимости из `requirements.txt`, если они появятся. |

Чтобы ограничить команду конкретными операциями, передай их имена через `OPERATIONS`.

```sh
make import OPERATIONS="AbortMultipartUpload ListObjectsV2"
```

При ошибке в отдельной статье скрипт продолжает обработку остальных и выводит команду для повторного запуска с нужными именами.

Оригинальные статьи Amazon Web Services распространяются по лицензии CC BY-SA 4.0, примеры кода — по MIT-0.

## Оглавление

- [AbortMultipartUpload](Docs/API/AbortMultipartUpload/README.md)
- [CompleteMultipartUpload](Docs/API/CompleteMultipartUpload/README.md)
- [CopyObject](Docs/API/CopyObject/README.md)
- [CreateBucket](Docs/API/CreateBucket/README.md)
- [CreateBucketMetadataConfiguration](Docs/API/CreateBucketMetadataConfiguration/README.md)
- [CreateBucketMetadataTableConfiguration](Docs/API/CreateBucketMetadataTableConfiguration/README.md)
- [CreateMultipartUpload](Docs/API/CreateMultipartUpload/README.md)
- [CreateSession](Docs/API/CreateSession/README.md)
- [DeleteBucket](Docs/API/DeleteBucket/README.md)
- [DeleteBucketAnalyticsConfiguration](Docs/API/DeleteBucketAnalyticsConfiguration/README.md)
- [DeleteBucketCors](Docs/API/DeleteBucketCors/README.md)
- [DeleteBucketEncryption](Docs/API/DeleteBucketEncryption/README.md)
- [DeleteBucketIntelligentTieringConfiguration](Docs/API/DeleteBucketIntelligentTieringConfiguration/README.md)
- [DeleteBucketInventoryConfiguration](Docs/API/DeleteBucketInventoryConfiguration/README.md)
- [DeleteBucketLifecycle](Docs/API/DeleteBucketLifecycle/README.md)
- [DeleteBucketMetadataConfiguration](Docs/API/DeleteBucketMetadataConfiguration/README.md)
- [DeleteBucketMetadataTableConfiguration](Docs/API/DeleteBucketMetadataTableConfiguration/README.md)
- [DeleteBucketMetricsConfiguration](Docs/API/DeleteBucketMetricsConfiguration/README.md)
- [DeleteBucketOwnershipControls](Docs/API/DeleteBucketOwnershipControls/README.md)
- [DeleteBucketPolicy](Docs/API/DeleteBucketPolicy/README.md)
- [DeleteBucketReplication](Docs/API/DeleteBucketReplication/README.md)
- [DeleteBucketTagging](Docs/API/DeleteBucketTagging/README.md)
- [DeleteBucketWebsite](Docs/API/DeleteBucketWebsite/README.md)
- [DeleteObject](Docs/API/DeleteObject/README.md)
- [DeleteObjectAnnotation](Docs/API/DeleteObjectAnnotation/README.md)
- [DeleteObjects](Docs/API/DeleteObjects/README.md)
- [DeleteObjectTagging](Docs/API/DeleteObjectTagging/README.md)
- [DeletePublicAccessBlock](Docs/API/DeletePublicAccessBlock/README.md)
- [GetBucketAbac](Docs/API/GetBucketAbac/README.md)
- [GetBucketAccelerateConfiguration](Docs/API/GetBucketAccelerateConfiguration/README.md)
- [GetBucketAcl](Docs/API/GetBucketAcl/README.md)
- [GetBucketAnalyticsConfiguration](Docs/API/GetBucketAnalyticsConfiguration/README.md)
- [GetBucketCors](Docs/API/GetBucketCors/README.md)
- [GetBucketEncryption](Docs/API/GetBucketEncryption/README.md)
- [GetBucketIntelligentTieringConfiguration](Docs/API/GetBucketIntelligentTieringConfiguration/README.md)
- [GetBucketInventoryConfiguration](Docs/API/GetBucketInventoryConfiguration/README.md)
- [GetBucketLifecycle](Docs/API/GetBucketLifecycle/README.md)
- [GetBucketLifecycleConfiguration](Docs/API/GetBucketLifecycleConfiguration/README.md)
- [GetBucketLocation](Docs/API/GetBucketLocation/README.md)
- [GetBucketLogging](Docs/API/GetBucketLogging/README.md)
- [GetBucketMetadataConfiguration](Docs/API/GetBucketMetadataConfiguration/README.md)
- [GetBucketMetadataTableConfiguration](Docs/API/GetBucketMetadataTableConfiguration/README.md)
- [GetBucketMetricsConfiguration](Docs/API/GetBucketMetricsConfiguration/README.md)
- [GetBucketNotification](Docs/API/GetBucketNotification/README.md)
- [GetBucketNotificationConfiguration](Docs/API/GetBucketNotificationConfiguration/README.md)
- [GetBucketOwnershipControls](Docs/API/GetBucketOwnershipControls/README.md)
- [GetBucketPolicy](Docs/API/GetBucketPolicy/README.md)
- [GetBucketPolicyStatus](Docs/API/GetBucketPolicyStatus/README.md)
- [GetBucketReplication](Docs/API/GetBucketReplication/README.md)
- [GetBucketRequestPayment](Docs/API/GetBucketRequestPayment/README.md)
- [GetBucketTagging](Docs/API/GetBucketTagging/README.md)
- [GetBucketVersioning](Docs/API/GetBucketVersioning/README.md)
- [GetBucketWebsite](Docs/API/GetBucketWebsite/README.md)
- [GetObject](Docs/API/GetObject/README.md)
- [GetObjectAcl](Docs/API/GetObjectAcl/README.md)
- [GetObjectAnnotation](Docs/API/GetObjectAnnotation/README.md)
- [GetObjectAttributes](Docs/API/GetObjectAttributes/README.md)
- [GetObjectLegalHold](Docs/API/GetObjectLegalHold/README.md)
- [GetObjectLockConfiguration](Docs/API/GetObjectLockConfiguration/README.md)
- [GetObjectRetention](Docs/API/GetObjectRetention/README.md)
- [GetObjectTagging](Docs/API/GetObjectTagging/README.md)
- [GetObjectTorrent](Docs/API/GetObjectTorrent/README.md)
- [GetPublicAccessBlock](Docs/API/GetPublicAccessBlock/README.md)
- [HeadBucket](Docs/API/HeadBucket/README.md)
- [HeadObject](Docs/API/HeadObject/README.md)
- [ListBucketAnalyticsConfigurations](Docs/API/ListBucketAnalyticsConfigurations/README.md)
- [ListBucketIntelligentTieringConfigurations](Docs/API/ListBucketIntelligentTieringConfigurations/README.md)
- [ListBucketInventoryConfigurations](Docs/API/ListBucketInventoryConfigurations/README.md)
- [ListBucketMetricsConfigurations](Docs/API/ListBucketMetricsConfigurations/README.md)
- [ListBuckets](Docs/API/ListBuckets/README.md)
- [ListDirectoryBuckets](Docs/API/ListDirectoryBuckets/README.md)
- [ListMultipartUploads](Docs/API/ListMultipartUploads/README.md)
- [ListObjectAnnotations](Docs/API/ListObjectAnnotations/README.md)
- [ListObjects](Docs/API/ListObjects/README.md)
- [ListObjectsV2](Docs/API/ListObjectsV2/README.md)
- [ListObjectVersions](Docs/API/ListObjectVersions/README.md)
- [ListParts](Docs/API/ListParts/README.md)
- [PutBucketAbac](Docs/API/PutBucketAbac/README.md)
- [PutBucketAccelerateConfiguration](Docs/API/PutBucketAccelerateConfiguration/README.md)
- [PutBucketAcl](Docs/API/PutBucketAcl/README.md)
- [PutBucketAnalyticsConfiguration](Docs/API/PutBucketAnalyticsConfiguration/README.md)
- [PutBucketCors](Docs/API/PutBucketCors/README.md)
- [PutBucketEncryption](Docs/API/PutBucketEncryption/README.md)
- [PutBucketIntelligentTieringConfiguration](Docs/API/PutBucketIntelligentTieringConfiguration/README.md)
- [PutBucketInventoryConfiguration](Docs/API/PutBucketInventoryConfiguration/README.md)
- [PutBucketLifecycle](Docs/API/PutBucketLifecycle/README.md)
- [PutBucketLifecycleConfiguration](Docs/API/PutBucketLifecycleConfiguration/README.md)
- [PutBucketLogging](Docs/API/PutBucketLogging/README.md)
- [PutBucketMetricsConfiguration](Docs/API/PutBucketMetricsConfiguration/README.md)
- [PutBucketNotification](Docs/API/PutBucketNotification/README.md)
- [PutBucketNotificationConfiguration](Docs/API/PutBucketNotificationConfiguration/README.md)
- [PutBucketOwnershipControls](Docs/API/PutBucketOwnershipControls/README.md)
- [PutBucketPolicy](Docs/API/PutBucketPolicy/README.md)
- [PutBucketReplication](Docs/API/PutBucketReplication/README.md)
- [PutBucketRequestPayment](Docs/API/PutBucketRequestPayment/README.md)
- [PutBucketTagging](Docs/API/PutBucketTagging/README.md)
- [PutBucketVersioning](Docs/API/PutBucketVersioning/README.md)
- [PutBucketWebsite](Docs/API/PutBucketWebsite/README.md)
- [PutObject](Docs/API/PutObject/README.md)
- [PutObjectAcl](Docs/API/PutObjectAcl/README.md)
- [PutObjectAnnotation](Docs/API/PutObjectAnnotation/README.md)
- [PutObjectLegalHold](Docs/API/PutObjectLegalHold/README.md)
- [PutObjectLockConfiguration](Docs/API/PutObjectLockConfiguration/README.md)
- [PutObjectRetention](Docs/API/PutObjectRetention/README.md)
- [PutObjectTagging](Docs/API/PutObjectTagging/README.md)
- [PutPublicAccessBlock](Docs/API/PutPublicAccessBlock/README.md)
- [RenameObject](Docs/API/RenameObject/README.md)
- [RestoreObject](Docs/API/RestoreObject/README.md)
- [SelectObjectContent](Docs/API/SelectObjectContent/README.md)
- [UpdateBucketMetadataAnnotationTableConfiguration](Docs/API/UpdateBucketMetadataAnnotationTableConfiguration/README.md)
- [UpdateBucketMetadataInventoryTableConfiguration](Docs/API/UpdateBucketMetadataInventoryTableConfiguration/README.md)
- [UpdateBucketMetadataJournalTableConfiguration](Docs/API/UpdateBucketMetadataJournalTableConfiguration/README.md)
- [UpdateObjectEncryption](Docs/API/UpdateObjectEncryption/README.md)
- [UploadPart](Docs/API/UploadPart/README.md)
- [UploadPartCopy](Docs/API/UploadPartCopy/README.md)
- [WriteGetObjectResponse](Docs/API/WriteGetObjectResponse/README.md)
