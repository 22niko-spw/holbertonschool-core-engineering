#!/usr/bin/env python3
"""WebSocket server with broadcast message handling."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def broadcast(message):
    """Send a message to all connected clients, skipping dead ones."""
    dead_clients = set()
    for client in connected_clients:
        try:
            await client.send(message)
        except ConnectionClosed:
            dead_clients.add(client)
    connected_clients.difference_update(dead_clients)


async def connection_handler(websocket):
    """Track the client and broadcast every message it sends."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the broadcast WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
