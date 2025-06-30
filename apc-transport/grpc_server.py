import grpc
from concurrent import futures
from apc_core.messages import apc_pb2, apc_pb2_grpc
from apc_core.state_machine import Conductor

class APCServicer(apc_pb2_grpc.APCServicer):
    def __init__(self, conductor):
        self.conductor = conductor

    def ProposeTask(self, request, context):
        # Example: handle ProposeTask message
        self.conductor.on_new_batch_goal(request.base.batch_id, [request.step_name])
        return apc_pb2.Accept(base=request.base, step_name=request.step_name)

    # Implement other RPCs as needed

def serve():
    conductor = Conductor()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    apc_pb2_grpc.add_APCServicer_to_server(APCServicer(conductor), server)
    server.add_insecure_port('[::]:50051')
    print("APC gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
