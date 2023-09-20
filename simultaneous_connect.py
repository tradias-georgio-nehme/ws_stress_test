import datetime
import asyncio
import plotly.express as plt
import plotly.offline as pyo
from ws_connection import connect_ws_delayed


async def simultaneous_connect(number_of_connections: int, max_msg: int, name: str, url: str, token: str, subscription):
    tasks = []
    messages = {}
    time_to_connect = []
    start_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc) + datetime.timedelta(seconds=1)
    for index in range(number_of_connections):
        tasks.append(asyncio.create_task(
            connect_ws_delayed(start_time=start_time, messages=messages, max_msg=max_msg, token=token, url=url,
                               subscription=subscription)))
    await asyncio.gather(*tasks)
    print(f"Number of messages received {len(messages)}")
    for task in tasks:
        time_to_connect.append((task.result()))
    sorted_result = sorted(time_to_connect, key=lambda x: x[1])
    result = [(elapsed.total_seconds(), start) for elapsed, start in sorted_result]
    elapsed = [elapsed for elapsed, start in result]
    start = [start for elapsed, start in result]
    print("Started plotting")
    plot = plt.scatter(x=start, y=elapsed)
    plot.update_layout(
        title=f"Time to connect {number_of_connections} times to websocket and receive {max_msg} messages from each")
    plot.update_layout(xaxis_title="connection start time")
    plot.update_layout(yaxis_title="Time to connect to websocket (seconds)")
    pyo.plot(plot, filename=f"{name}_time_to_connect_{number_of_connections}_times_{max_msg}_messages_each.html")
