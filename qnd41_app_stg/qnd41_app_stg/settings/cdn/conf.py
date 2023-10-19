import os
APP_NAME=os.environ.get("APP_NAME")
AWS_ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
#AWS_ACCESS_KEY= 'DO00DZXWWE3BKHHMG3NV'
#AWS_SECRET_ACCESS_KEY= '6ZDJ/K4xQ5g/GDGb40x4ojTNfGZbn0N7xvZ4QFqJ96w'
AWS_STORAGE_BUCKET_NAME=os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL=os.environ.get("AWS_S3_ENDPOINT_URL")
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_LOCATION="https://{ AWS_STORAGE_BUCKET_NAME }.{ AWS_S3_REGION_NAME }.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE="qnd41_app_stg.settings.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnd41_app_stg.settings.cdn.backends.StaticRootS3BotoStorage"






#STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_STATIC_LOCATION = 'staticfiles'