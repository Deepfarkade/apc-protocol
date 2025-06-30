"""
APC WebSocket Transport Adapter (Python)
Stub for async WebSocket server/client using websockets library.
"""
import asyncio
# import websockets

class APCWebSocketTransport:
    def __init__(self, agent, host='localhost', port=8765):
        self.agent = agent
        self.host = host
        self.port = port

    async def handler(self, websocket, path):
        async for message in websocket:
            # Deserialize and route message to agent
            pass

    def start(self):
        # asyncio.get_event_loop().run_until_complete(
        #     websockets.serve(self.handler, self.host, self.port)
        # )
        # asyncio.get_event_loop().run_forever()
        pass
