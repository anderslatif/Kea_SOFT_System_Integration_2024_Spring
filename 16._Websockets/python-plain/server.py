import asyncio
import websockets

async def handle_new_websocket(websocket, path):
    print("Client connected")
    try:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

            response = f"Received: {message}"
            await websocket.send(response)
    except websockets.ConnectionClosed:
        print("Client disconnected")

if __name__ == "__main__":
    # Start the WebSocket server
    # Port 8765 would be standard
    start_server = websockets.serve(handle_new_websocket, "localhost", 8000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

