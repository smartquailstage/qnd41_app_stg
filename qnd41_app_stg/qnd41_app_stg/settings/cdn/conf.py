import os
APP_NAME="qnd41_app_stg"
AWS_ACCESS_KEY="DO00YMUG6DLFPMDZFZWH"
AWS_SECRET_ACCESS_KEY="m6qRI/NFF+moVsoSoU/CdvQOKlsAr4BIXTHWn057Tiw"
#AWS_ACCESS_KEY= 'DO00DZXWWE3BKHHMG3NV'
#AWS_SECRET_ACCESS_KEY= '6ZDJ/K4xQ5g/GDGb40x4ojTNfGZbn0N7xvZ4QFqJ96w'
AWS_STORAGE_BUCKET_NAME="qnd41-app-staticfiles"
AWS_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com/"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}
AWS_S3_REGION_NAME = "nyc3"
AWS_LOCATION="https://{ AWS_STORAGE_BUCKET_NAME }.{ AWS_S3_REGION_NAME }.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE="qnd41_app_stg.settings.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnd41_app_stg.settings.cdn.backends.StaticRootS3BotoStorage"






#STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_STATIC_LOCATION = 'staticfiles'