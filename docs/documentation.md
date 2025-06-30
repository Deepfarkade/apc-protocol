# APC Documentation

Welcome to the official documentation for the Agent Protocol Conductor (APC)!

---

## Table of Contents
- [Introduction](#introduction)
- [Design Rationale & Goals](#design-rationale--goals)
- [Architecture Overview](#architecture-overview)
- [Message Schemas](#message-schemas)
- [State Machines](#state-machines)
- [Checkpointing & Failover](#checkpointing--failover)
- [Transport Adapters](#transport-adapters)
- [Security & Policy](#security--policy)
- [Registry & Discovery](#registry--discovery)
- [SDK Usage](#sdk-usage)
- [Examples](#examples)
- [FAQ](#faq)

---

## Introduction
APC is a decentralized orchestration protocol for heterogeneous AI agent ecosystems. It enables dynamic leadership hand-off, sequenced task execution, checkpointing, failover, and auditability—all without centralized control.

---

## Design Rationale & Goals
- **Decentralized Leadership**: No single point of failure; any agent can become conductor.
- **Dynamic Sequencing**: Workflows defined at runtime, supporting evolving subtask lists.
- **Resilience & Checkpointing**: Recover from agent failures via checkpoints and takeover.
- **Interoperability**: Protobuf/JSON schemas for cross-language support.
- **Extensibility & Security**: Add new message types, mTLS/JWT, and policy enforcement.

---

## Architecture Overview
```
+-------------+   +-------------+   +-------------+
|  Agent A    |<->|  Message    |<->|  Agent B    |
| (Conductor) |   |  Transport  |   |  (Worker)   |
+-------------+   +-------------+   +-------------+
      |  /                                 
      | \                                  
      v  v                                 
+-------------+ Registry/Discovery +-------------+
|  Agent C    |<-------------------|  Agent D    |
| (Worker)    |                    |  (Planner)  |
+-------------+                    +-------------+
```
- **Registry/Discovery**: Optional central or P2P service for agent registration and discovery.
- **Transport Layer**: gRPC or WebSocket for bi-directional messaging.
- **Message Broker**: Pub/Sub or direct peer connections.

---

## Message Schemas
- Defined in [apc-proto/apc.proto](../apc-proto/apc.proto)
- Protobuf v3 for cross-language support
- Core messages: `ProposeTask`, `Accept`, `Reject`, `Completed`, `Failed`, `TakeOver`, etc.

---

## State Machines
- **Conductor**: Handles batch goals, proposes tasks, sequences steps, manages failover.
- **Worker**: Accepts/rejects tasks, executes, reports completion/failure.
- **CheckpointManager**: Saves and restores state for resilience.

---

## Checkpointing & Failover
- Pluggable backends: In-memory, Redis, S3
- Auto-checkpointing and recovery logic
- TakeOver messages for dynamic leadership

---

## Transport Adapters
- gRPC: High-performance, strongly-typed
- WebSocket: Lightweight, browser-friendly
- Easily extendable for other transports

---

## Security & Policy
- mTLS: X.509 certificate-based mutual authentication
- JWT: Role/scopes encoded in tokens
- Policy engine for compliance and data sensitivity

---

## Registry & Discovery
- Optional: Register, discover, and load-balance agents
- Example: `registerAgent()`, `discoverAgents(filter)`

---

## SDK Usage
- See [examples/](../examples/) for sample agents
- Subclass `Conductor` or `Worker` and implement your logic
- Integrate LLMs or custom business logic as needed

---

## Examples
- [Minimal gRPC Conductor/Worker](../examples/grpc_minimal.py)
- [LLM Worker Integration](../examples/llm_worker.py)

---

## FAQ
**Q: Can I use APC with Node.js, Go, or Java?**
A: Yes! Use the Protobuf schema to generate SDKs for any language.

**Q: How do I add a new message type?**
A: Extend the Protobuf schema and regenerate code.

**Q: How do I contribute?**
A: Fork the repo, branch, and submit a PR!

---

For more, see the [README](../README.md) or open an issue/discussion on GitHub.
