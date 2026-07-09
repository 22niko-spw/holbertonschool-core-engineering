#!/usr/bin/env python3
"""WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server, send one message, return the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Connect to the local echo server and print its response."""
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
