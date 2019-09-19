from __future__ import print_function
import json
import boto3
import time
import urllib

print("Loading function")

s3Client = boto3.client('s3')
s3 = boto3.resource('s3')
target_bucket = 'dp-demo-1'
tmp_dir = 'temp'


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    copy_source = {'Bucket': source_bucket, 'Key': key}
    print("SOURCE_BUCKET", source_bucket)
    print("TARGET_BUCKET", target_bucket)
    print("KEY", key)
    print("COPY_SOURCE", copy_source)

    try:
        #target_key = key
        target_key = key.split("/", 1)[1]
        target_key = tmp_dir + '/' + target_key
        print("TARGET_KEY:", target_key)
        if not key.startswith('temp'):
            print("Waiting for the file persist in the source bucket")
            waiter = s3Client.get_waiter('object_exists')
            waiter.wait(Bucket=source_bucket, Key=key)
            print("Copying object from source s3 bucket to target s3 bucket")
            s3.meta.client.copy(copy_source, target_bucket, target_key)
            s3.Object(source_bucket, key).delete()

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, source_bucket))
        raise e
