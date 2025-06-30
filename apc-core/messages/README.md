# Instructions for generating Python code from Protobuf

# 1. Install protobuf compiler and Python plugin:
#    pip install grpcio-tools
#
# 2. Run the following command from the project root:
#    python -m grpc_tools.protoc -I=apc-proto --python_out=apc-core/messages --grpc_python_out=apc-core/messages apc-proto/apc.proto
#
# This will generate apc_pb2.py and apc_pb2_grpc.py in apc-core/messages/
