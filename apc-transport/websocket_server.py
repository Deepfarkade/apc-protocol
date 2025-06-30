import asyncio
import websockets
import json
from apc_core.state_machine import Worker

class APCWebSocketServer:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.worker = Worker()

    async def handler(self, websocket, path):
        async for message in websocket:
            data = json.loads(message)
            # Example: handle ProposeTask
            if data.get('type') == 'ProposeTask':
                self.worker.on_propose_task(data)
                await websocket.send(json.dumps({'type': 'Accept', 'step_name': data['step_name']}))

    def start(self):
        print(f"APC WebSocket server running on ws://{self.host}:{self.port}")
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(self.handler, self.host, self.port)
        )
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    APCWebSocketServer().start()
