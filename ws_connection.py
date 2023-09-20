import datetime
import websockets
import orjson

from datetime_converter import tz_to_timestamp


async def connect_ws_delayed(start_time: datetime.datetime, messages: dict, max_msg: int, token: str, url: str,
                             subscription: str):
    extra_headers = {'x-token-id': token}
    connection_start_time = datetime.datetime.utcnow()
    async for websocket in websockets.connect(url, extra_headers=extra_headers, timeout=99999999):
        elapsed_time = datetime.datetime.utcnow() - connection_start_time
        await websocket.send(subscription)
        counter = 0
        while True:
            msg = await websocket.recv()
            msg_json = orjson.loads(msg)
            # print(msg_json)
            if 'timestamp' in msg_json:
                msg_json['timestamp'] = tz_to_timestamp(msg_json['timestamp'])
                if msg_json['timestamp'] >= start_time:
                    messages[msg_json['timestamp']] = msg_json
                    counter = counter + 1
                    if counter == max_msg:
                        break
        return elapsed_time, connection_start_time
