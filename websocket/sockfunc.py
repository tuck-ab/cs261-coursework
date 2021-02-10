import asyncio 
import json

connections = set()


async def func(websocket, path):
    connections.add(websocket)
    try:
        while True:
            msg = await websocket.recv()
            
            data = json.loads(msg)

            to_return = data["name"] + " sent: " + data["msg"]

            for conn in connections:
                await conn.send(to_return)
    finally:
        connections.remove(websocket)
        print("disconnected")
