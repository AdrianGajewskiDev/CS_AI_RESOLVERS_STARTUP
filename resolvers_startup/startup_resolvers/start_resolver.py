from resolvers_startup._lambda.invoke_lambda import invoke_lambda
from resolvers_startup.logging.logger import InternalLogger


def start_resolver(resolver: str, payload: dict) -> None:
    InternalLogger.LogDebug(f"Starting resolver: {resolver}")
    try:
        invoke_lambda(resolver, payload)
    except Exception as e:
        InternalLogger.LogError(f"Error while starting resolver: {resolver}. Error: {str(e)}")
        raise e