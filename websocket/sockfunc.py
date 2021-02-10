import asyncio 
import json


async def func(websocket, path):
    try:
        while True:
            msg = await websocket.recv()
            
            print(msg)

    finally:
        pass
