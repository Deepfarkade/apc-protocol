# APC: Agent Protocol Conductor

APC is a decentralized orchestration protocol and SDK for heterogeneous AI agent ecosystems. It enables dynamic leadership hand-off, sequenced task execution, checkpointing, failover, and auditability—without centralized control.

## Features
- Protobuf-based message schemas for interoperability
- Pluggable checkpoint manager (in-memory, Redis, S3)
- State machine engine for conductor and worker agents
- gRPC and WebSocket transport adapters
- Security stubs (mTLS, JWT)
- Ready for open source and multi-language SDKs

## Quick Start

1. Install the package (editable mode for development):
   ```sh
   pip install -e ./apc-core
   ```
2. Generate Python code from Protobuf:
   ```sh
   python -m grpc_tools.protoc -I=apc-proto --python_out=apc-core/messages --grpc_python_out=apc-core/messages apc-proto/apc.proto
   ```
3. Run a sample agent (see `samples/python/`)

## Onboarding Automation

### 1. Install the core package (editable mode):
   ```sh
   python install_editable.py
   ```

### 2. Generate Python code from Protobuf:
   ```sh
   python generate_proto.py
   ```

### 3. Run a sample agent (see `examples/` or `samples/python/`):
   ```sh
   python examples/grpc_minimal.py
   ```

## Getting Started (Step-by-Step)

### 1. Clone the repository
```sh
# Clone the repo and enter the directory
 git clone <your-repo-url>
 cd APC
```

### 2. Install Python dependencies and the core package (editable mode)
```sh
python install_editable.py
```
This makes the `apc_core` package available everywhere in your environment for development and usage.

### 3. Generate Python code from Protobuf schemas
```sh
python generate_proto.py
```
This will generate all message and gRPC classes in `apc-core/messages/`.

### 4. Run an example agent
```sh
python examples/grpc_minimal.py
```
This will start a minimal Conductor and Worker agent using the APC protocol over gRPC.

---

## Advanced Usage
- Integrate LLMs or custom logic in your Worker agents (see `examples/llm_worker.py`).
- Use Redis or S3 for distributed checkpointing.
- Build your own CLI or web dashboard on top of the protocol.

## Troubleshooting
- If you see import errors, make sure you ran `python install_editable.py` and `python generate_proto.py`.
- For IDEs, ensure your workspace root is the project root so relative imports resolve.

## Project Structure
- `apc-core/` — Core Python SDK
- `apc-proto/` — Protobuf schemas
- `apc-transport/` — gRPC/WebSocket adapters
- `samples/` — Example agents
- `tests/` — Integration tests

## Contributing
- Fork, branch, and submit PRs!
- See `apc-proto/apc.proto` for message definitions
- See `apc-core/README.md` for architecture

## License
MIT
