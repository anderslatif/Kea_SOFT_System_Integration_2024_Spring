import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Ping")
        print(await websocket.recv())

# asyncio.get_event_loop().run_until_complete(hello())
# After Python 3.7 you can no do this:
asyncio.run(hello())