from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage


    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class DocumentStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class ImageSettingsStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

else:
    from storages.backends.s3boto3 import S3Boto3Storage


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIA_LOCATION
        file_overwrite = False
        default_acl = 'public-read'


    class DocumentStorage(S3Boto3Storage):
        location = settings.DOCUMENT_LOCATION
        file_overwrite = False
        default_acl = 'public-read'


    class ImageSettingsStorage(S3Boto3Storage):
        location = settings.IMAGE_SETTINGS_LOCATION
        file_overwrite = False
        default_acl = 'public-read'