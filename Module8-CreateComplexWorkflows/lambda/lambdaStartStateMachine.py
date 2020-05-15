import boto3
import json
import uuid

STEP_FUNCTION_ARN = "" # <--- CHANGE ME

stepfunctions = boto3.client('stepfunctions')

def lambda_handler(event, context):
    print("Received event: \n" + str(event))
    
    for record in event['Records']:
        
        response = stepfunctions.start_execution(
            stateMachineArn=STEP_FUNCTION_ARN,
            name=str(uuid.uuid4()),
            input=json.dumps(record)
        )