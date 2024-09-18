from resolvers_startup.startup_resolvers.startup import startup


def handler(event: dict, context):
    return startup(event)