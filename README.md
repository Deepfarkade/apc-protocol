# ![APC Logo](https://raw.githubusercontent.com/deepfarkade/apc-protocol/main/docs/images/apc-logo.png)

# APC: Agent Protocol Conductor

[![PyPI version](https://img.shields.io/pypi/v/apc-core?color=blue)](https://pypi.org/project/apc-core/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/deepfarkade/apc-protocol/ci.yml?branch=main)](https://github.com/deepfarkade/apc-protocol/actions)
[![Docs](https://img.shields.io/badge/docs-online-blue)](docs/documentation.md)

A protocol for decentralized, resilient, and auditable orchestration of heterogeneous AI agent ecosystems.

[Documentation](docs/documentation.md) | [Specification](apc-proto/apc.proto) | [Discussions](https://github.com/deepfarkade/apc-protocol/discussions)

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

## 📦 Release Information

- **Current Release:** v0.1.x (Alpha)
- See [Releases](https://github.com/deepfarkade/apc-protocol/releases) for changelogs and version history.
- This is the first public alpha release of the APC protocol and SDK.

---

## 🧠 Why APC? (The Evolutionary Backdrop)

**MCP (Message-Centered Protocol)** gave agents a common language for basic send/receive—everyone could talk, but only at the lowest level.

**A2A (Agent-to-Agent)** enabled direct peer-to-peer links, letting Agent A push subtasks straight to Agent B. This improved speed, but made systems brittle at scale.

**ACP (Agent Control Protocol)** introduced a central orchestrator to sequence tasks and enforce policies. This fixed deadlocks, but reintroduced a single point of failure and made most agents passive workers.

All three advanced the field, but none provided a flexible, fault-tolerant way for agents to coordinate and think for themselves in complex, branching workflows.

---

## 🚀 Why APC Is the Next Leap

- **Distributed “Conductors”**: Any agent can temporarily assume the conductor role for a workflow, enabling sequencing, dependency checks, and deadlock avoidance—without a heavy, central master.
- **Plug-and-Play Orchestration**: Agents register their orchestration capabilities and load. If one goes offline, another takes over automatically.
- **Context-Aware Scheduling**: Conductors probe agent readiness, context, and load before launching subtasks, avoiding mid-pipeline failures.
- **Graceful Preemption & Handoffs**: When priorities shift, conductors checkpoint running subtasks and offer them to peers—no more “hung” workflows.

---

## 🌟 The Transformative Impact

- **Elastic Workflows**: Agents can dynamically lead or follow, adapting to changing needs.
- **No Orchestration Silos**: Get the governance of ACP without the latency or single-point-of-failure risk.
- **Simplified Developer Experience**: Define tasks and dependencies once—APC’s conductor handshakes handle the rest.

**In short:** APC doesn’t just mediate “who talks to whom”; it embeds a living, breathing conductor in every agent ecosystem—unlocking true multi-agent creativity, resilience, and scale. That’s why APC is the next flagship protocol for Gen-AI agents.

---

## **Example: Document Processing Workflow with APC**

Imagine a real-world scenario where you need to process a batch of scanned documents:

- `Agent A` (Conductor): Orchestrates the workflow.
- `Agent B` (Worker: OCR): Extracts text from images.
- `Agent C` (Worker: Summarizer): Summarizes the extracted text.

**Workflow:**
1. `Agent A` receives a new batch and proposes the first step to `Agent B` (OCR).
2. `Agent B` accepts, processes the images, and sends back the extracted text.
3. `Agent A` checkpoints the result, then proposes the next step to `Agent C` (Summarization).
4. `Agent C` summarizes the text and returns the summary to `Agent A`.
5. If `Agent B` fails or disconnects, APC's checkpointing and takeover logic allow another eligible OCR agent to resume from the last checkpoint—no data loss, no manual intervention.
6. Every step, hand-off, and result is auditable and interoperable across languages and platforms.

---

## 📊 More Real-World Scenarios & Diagrams

For advanced diagrams and multi-agent workflow scenarios, see the [full documentation](docs/documentation.md).

---

## 🛡️ License
MIT
