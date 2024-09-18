import json
import boto3

def invoke_lambda(resolver: str, payload: dict) -> None:
    lambda_client = boto3.client('lambda')
    lambda_client.invoke(
        FunctionName=resolver,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )