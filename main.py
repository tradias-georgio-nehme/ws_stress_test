import asyncio

from simultaneous_connect import simultaneous_connect


async def main_task_last_test(token: str, url: str, name: str, subscription_message: str, max_messages: int,
                              max_connections: int):
    await simultaneous_connect(max_connections, max_messages, token=token, url=url, name=name,
                               subscription=subscription_message)


def main(token: str, url: str, subscription_message: str, max_messages: int, max_connections: int, websocket_name: str):
    """
    :param token: websocket authentication token
    :param url: websocket URL
    :param subscription_message: prices channel subscription message
    :param max_messages: number of messages per connection
    :param max_connections: number of concurrent connections
    :param websocket_name: name to be added to the name of the plot
    """
    asyncio.run(
        main_task_last_test(token=token, url=url, name=websocket_name, subscription_message=subscription_message,
                            max_messages=max_messages, max_connections=max_connections))


if __name__ == '__main__':
    WEBSOCKET_NAME = ''
    TOKEN = ''
    URL = ''
    SUBSCRIPTION_MESSAGE = ''
    MAX_MESSAGES = 10
    MAX_CONNECTIONS = 500

    main(
        websocket_name=WEBSOCKET_NAME,
        token=TOKEN,
        url=URL,
        subscription_message=SUBSCRIPTION_MESSAGE,
        max_messages=MAX_MESSAGES,
        max_connections=MAX_CONNECTIONS
    )
