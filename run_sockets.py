import websocket

import asyncio
import websockets 

start_server = websockets.serve(websocket.func, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()