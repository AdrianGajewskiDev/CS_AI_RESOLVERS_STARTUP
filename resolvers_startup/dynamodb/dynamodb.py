import os
import boto3

TASK_TABLE_NAME = os.getenv("TASK_TABLE_NAME", "")

def update_status(task_id: str, created_at: str, status: str) -> None:
    dynamodb = boto3.client("dynamodb")
    dynamodb.update_item(
        TableName=TASK_TABLE_NAME,
        Key={
            "task_id": {"S": task_id},
            "created_date": {"S": created_at}  # Replace with actual range key value
        },
        UpdateExpression="SET #status = :status",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={":status": {"S": status}},
    )