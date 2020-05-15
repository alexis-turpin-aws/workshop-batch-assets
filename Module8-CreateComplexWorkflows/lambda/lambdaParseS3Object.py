import boto3
import json

s3 = boto3.client('s3')
    
def lambda_handler(event, context):
    print("Received event: \n" + str(event))
    
    bucket = event['s3']['bucket']['name']
    key = event['s3']['object']['key']
    stocks_file = s3.get_object(Bucket=bucket, Key=key)
    content = stocks_file['Body'].read().decode('utf-8')
        
    return content.splitlines()