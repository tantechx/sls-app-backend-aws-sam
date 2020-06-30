import boto3
import os
import json

def handler(event, context):
    ddb = boto3.resource('dynamodb',endpoint_url='http://dynamodb:8000')
    table = ddb.Table(os.environ.get('DDB_TABLE_NAME'))
    try:
        print(table)
        response = table.scan()
        
        data = response['Items']
        return {
            'statusCode': 200,
            "isBase64Encoded": False,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },      
            'body': json.dumps(data,ensure_ascii=False)
        }
    except Exception as e:
        print(e)