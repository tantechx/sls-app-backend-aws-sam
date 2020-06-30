import uuid
import boto3
import os
import json

s3 = boto3.client('s3')

def get_upload_url():
    action_id = uuid.uuid4()
    s3_params = {
        "Bucket": os.environ.get('UploadBucket'),
        "Key": f'''{action_id}.jpg''',
        "ContentType": 'image/jpeg'
    }
    print('get_upload_url:',s3_params)
    return {
            "statusCode": 200,
            "isBase64Encoded": False,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "uploadURL": s3.generate_presigned_url('put_object', s3Params),
                "photoFilename": f'''${action_id}.jpg'''
            })
        }

def handler(event, context):
    result = get_upload_url()
    print('Result:',result)
    return result