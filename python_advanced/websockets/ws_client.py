#!/usr/bin/env python3
"""WebSocket client."""
import asyncio
import os
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server, send one message, return the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Connect to the server (via WS_URI if set) and print its response."""
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
