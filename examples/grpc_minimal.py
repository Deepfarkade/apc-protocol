"""
Example: Minimal APC Conductor and Worker agents communicating via gRPC.
This demonstrates how to use the APC protocol stack in a real workflow.
"""
import threading
import time
import grpc
from concurrent import futures
from apc_core.messages import apc_pb2, apc_pb2_grpc
from apc_core.state_machine import Conductor, Worker

# --- Worker gRPC Server ---
class WorkerServicer(apc_pb2_grpc.APCServicer):
    def __init__(self, worker):
        self.worker = worker
    def ProposeTask(self, request, context):
        self.worker.on_propose_task(request)
        return apc_pb2.Accept(base=request.base, step_name=request.step_name)

# --- Conductor gRPC Client ---
def run_conductor():
    conductor = Conductor()
    channel = grpc.insecure_channel('localhost:50052')
    stub = apc_pb2_grpc.APCStub(channel)
    # Simulate a workflow with two steps
    for step in ["step1", "step2"]:
        base = apc_pb2.BaseMessage(batch_id="batch-001", sender_id="conductor", timestamp=int(time.time()))
        propose = apc_pb2.ProposeTask(base=base, step_name=step, role="conductor")
        response = stub.ProposeTask(propose)
        print(f"Conductor: got response {response}")
        conductor.on_accept(step)
        conductor.on_completed(step)

# --- Worker gRPC Server Thread ---
def run_worker():
    worker = Worker()
    server = grpc.server(threading.ThreadPoolExecutor(max_workers=2))
    apc_pb2_grpc.add_APCServicer_to_server(WorkerServicer(worker), server)
    server.add_insecure_port('[::]:50052')
    print("Worker gRPC server running on port 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    # Start worker in a thread, then run conductor
    t = threading.Thread(target=run_worker, daemon=True)
    t.start()
    time.sleep(1)
    run_conductor()
