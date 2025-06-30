# APC: Agent Protocol Conductor

---

<img src="https://raw.githubusercontent.com/deepfarkade/apc-protocol/main/docs/apc-logo.png" alt="APC Logo" width="120" align="right" />

A protocol for decentralized, resilient, and auditable orchestration of heterogeneous AI agent ecosystems.

[Documentation](#getting-started-step-by-step) | [Specification](apc-proto/apc.proto) | [Discussions](https://github.com/deepfarkade/apc-protocol/discussions)

---

APC (Agent Protocol Conductor) is an open protocol and SDK for orchestrating distributed AI agents, enabling dynamic leadership hand-off, sequenced task execution, checkpointing, failover, and auditability—without centralized control. APC is designed for interoperability, extensibility, and production-readiness, supporting both classic automation and LLM-powered agents.

---

## 🚀 Getting Started

- 📚 **Read the [Documentation](#getting-started-step-by-step)** for guides and tutorials
- 🔍 **Review the [Specification](apc-proto/apc.proto)** for protocol details
- 🧑‍💻 **Use our SDKs to start building:**
  - [Python SDK](apc-core/)
  - [TypeScript SDK](#) *(coming soon)*
  - [Java SDK](#) *(coming soon)*

---

## 🛠️ Features
- **Protobuf-based message schemas** for cross-language interoperability
- **Pluggable checkpoint manager** (in-memory, Redis, S3)
- **State machine engine** for conductor and worker agents
- **gRPC and WebSocket transport adapters**
- **Security stubs** (mTLS, JWT)
- **Ready for open source and multi-language SDKs**

---

## ⚡ Quick Start

```sh
# 1. Install the core package (editable mode)
python install_editable.py

# 2. Generate Python code from Protobuf
python generate_proto.py

# 3. Run a sample agent (see examples/ or samples/python/)
python examples/grpc_minimal.py
```

---

## 🧑‍💻 Getting Started (Step-by-Step)

1. **Clone the repository**
   ```sh
   git clone https://github.com/deepfarkade/apc-protocol.git
   cd apc-protocol
   ```
2. **Install Python dependencies and the core package (editable mode)**
   ```sh
   python install_editable.py
   ```
3. **Generate Python code from Protobuf schemas**
   ```sh
   python generate_proto.py
   ```
4. **Run an example agent**
   ```sh
   python examples/grpc_minimal.py
   ```

---

## 💡 Why is this easy?
- **No manual pip or protoc commands needed**: Just run the provided scripts.
- **Plug-and-play**: Add your own agents, LLMs, or business logic by subclassing the provided state machines.
- **Multi-language ready**: Use the same Protobuf schema to generate SDKs for Node.js, Go, etc.
- **Production-grade**: Pluggable checkpointing, security stubs, and transport adapters included.

---

## 🔥 Advanced Usage
- Integrate LLMs or custom logic in your Worker agents (see [`examples/llm_worker.py`](examples/llm_worker.py)).
- Use Redis or S3 for distributed checkpointing.
- Build your own CLI or web dashboard on top of the protocol.

---

## 🧩 Project Structure
- [`apc-core/`](apc-core/) — Core Python SDK
- [`apc-proto/`](apc-proto/) — Protobuf schemas
- [`apc-transport/`](apc-transport/) — gRPC/WebSocket adapters
- [`examples/`](examples/) — Example agents and LLM integration
- [`samples/`](samples/) — Additional sample agents
- [`tests/`](tests/) — Integration tests

---

## 🤝 Contributing
- Fork, branch, and submit PRs!
- See [`apc-proto/apc.proto`](apc-proto/apc.proto) for message definitions
- See [`apc-core/README.md`](apc-core/README.md) for architecture

---

## 🛡️ License
MIT
