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

**Visual Diagram:**

```mermaid
graph TD
    A[Agent A (Conductor)] <--> M[Message Transport]
    M <--> B[Agent B (Worker)]
    A -->|Registry/Discovery| C[Agent C (Worker)]
    C -->|Registry/Discovery| D[Agent D (Planner)]
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

## More Real-World Scenarios & Diagrams

### Scenario 1: Multi-Stage Data Pipeline

- `Agent X` (Conductor): Orchestrates ETL pipeline.
- `Agent Y` (Worker: Extract): Pulls data from APIs.
- `Agent Z` (Worker: Transform): Cleans and normalizes data.
- `Agent W` (Worker: Load): Loads data into a database.

**Data Flow:**

```mermaid
graph TD
    X[Agent X (Conductor)] -->|ProposeTask: Extract| Y[Agent Y (Extract)]
    Y -->|Completed: Raw Data| X
    X -->|ProposeTask: Transform| Z[Agent Z (Transform)]
    Z -->|Completed: Clean Data| X
    X -->|ProposeTask: Load| W[Agent W (Load)]
    W -->|Completed: DB Insert| X
    Y -.->|Failure/Timeout| X
    X -->|TakeOver| Y2[Agent Y2 (Backup Extract)]
    Y2 -->|Completed: Raw Data| X
```

---

### Scenario 2: LLM-Driven Multi-Agent Chat

- `Agent M` (Conductor): Manages conversation flow.
- `Agent N` (Worker: LLM): Generates responses.
- `Agent O` (Worker: Tool-Caller): Executes API/tool calls.

**Data Flow:**

```mermaid
graph TD
    M[Agent M (Conductor)] -->|ProposeTask: Generate| N[Agent N (LLM)]
    N -->|Completed: Response| M
    M -->|ProposeTask: ToolCall| O[Agent O (Tool-Caller)]
    O -->|Completed: Tool Result| M
    N -.->|Failure/Timeout| M
    M -->|TakeOver| N2[Agent N2 (Backup LLM)]
    N2 -->|Completed: Response| M
```

---

### Scenario 3: Distributed Image Processing Pipeline

- `Agent P` (Conductor): Orchestrates image processing.
- `Agent Q` (Worker: Preprocessor): Resizes and normalizes images.
- `Agent R` (Worker: Classifier): Classifies images.
- `Agent S` (Worker: Annotator): Annotates images with results.

**Data Flow:**

```mermaid
graph TD
    P[Agent P (Conductor)] -->|ProposeTask: Preprocess| Q[Agent Q (Preprocessor)]
    Q -->|Completed: Preprocessed Images| P
    P -->|ProposeTask: Classify| R[Agent R (Classifier)]
    R -->|Completed: Labels| P
    P -->|ProposeTask: Annotate| S[Agent S (Annotator)]
    S -->|Completed: Annotated Images| P
    Q -.->|Failure/Timeout| P
    P -->|TakeOver| Q2[Agent Q2 (Backup Preprocessor)]
    Q2 -->|Completed: Preprocessed Images| P
```

---

### Scenario 4: Autonomous Fleet Coordination

- `Agent F` (Conductor): Assigns delivery tasks.
- `Agent G` (Worker: Drone 1): Delivers package.
- `Agent H` (Worker: Drone 2): Delivers package.
- `Agent I` (Worker: Ground Robot): Handles last-mile delivery.

**Data Flow:**

```mermaid
graph TD
    F[Agent F (Conductor)] -->|ProposeTask: Deliver| G[Agent G (Drone 1)]
    F -->|ProposeTask: Deliver| H[Agent H (Drone 2)]
    G -->|Completed: Delivery| F
    H -->|Completed: Delivery| F
    F -->|ProposeTask: Last Mile| I[Agent I (Ground Robot)]
    I -->|Completed: Final Delivery| F
    G -.->|Failure/Timeout| F
    F -->|TakeOver| G2[Agent G2 (Backup Drone)]
    G2 -->|Completed: Delivery| F
```

---

For more, see the [README](../README.md) or use the provided Mermaid code in a compatible viewer. Each scenario demonstrates APC's ability to coordinate, recover, and audit complex, distributed agent workflows in real-world domains.
