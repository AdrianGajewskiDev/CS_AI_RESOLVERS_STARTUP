import ast
import json
import os

from resolvers_startup.dynamodb.dynamodb import update_status
from resolvers_startup.logging.logger import InternalLogger
from resolvers_startup.startup_resolvers.start_resolver import start_resolver

RESOLVERS = os.getenv("RESOLVER_NAMES", [])

def startup(event: dict) -> int:
    started = 0
    for record in event["Records"]:
        started += _process_record(record)

    InternalLogger.LogDebug(f"Started {started} resolver(s).")
    return started

def _process_record(record: dict) -> int:
    sns_message = json.loads(record["Sns"]["Message"])
    new_image = sns_message["dynamodb"]["NewImage"]
    seed_data = json.loads(new_image["seed_data"]["S"])
    task_id = new_image["task_id"]["S"]
    created_date = new_image["created_date"]["S"]

    payload = {
        "seed_data": seed_data,
        "task_id": task_id,
        "created_date": created_date
    }
    InternalLogger.LogDebug(f"Starting resolvers: {RESOLVERS}")
    InternalLogger.LogDebug(f"Starting resolvers with payload: {payload}")
    if not RESOLVERS:
        update_status(task_id, created_date, "FAILED")
        InternalLogger.LogError("No resolvers found. Exiting.")
        raise Exception("No resolvers found.")
    
    update_status(task_id, created_date, "GATHERING_DATA")
    
    for resolver in ast.literal_eval(RESOLVERS):
        start_resolver(resolver, payload)

    return len(RESOLVERS)

    