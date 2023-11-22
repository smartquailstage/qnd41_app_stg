import os

AWS_ACCESS_KEY="DO00H9RAWAG3RCAXZL4B"
AWS_SECRET_ACCESS_KEY="NIoTCfQJWtl9se9b17CIFey5YM15lJsj7ULMovkGgok"
AWS_STORAGE_BUCKET_NAME='qnode41'
AWS_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com/"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}

AWS_LOCATION="https://qnode41.nyc3.digitaloceanspaces.com"
#STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/static/'
DEFAULT_FILE_STORAGE="qnd41_app_stg.settings.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnd41_app_stg.settings.cdn.backends.StaticRootS3BotoStorage"
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





#STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_STATIC_LOCATION = 'staticfiles'

#STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_STATIC_LOCATION = 'staticfiles'