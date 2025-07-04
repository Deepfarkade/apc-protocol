# ![APC Logo](https://raw.githubusercontent.com/deepfarkade/apc-protocol/main/docs/images/apc-logo.png)

# APC: Agent Protocol Conductor

[![PyPI version](https://img.shields.io/pypi/v/apc-protocol?color=blue)](https://pypi.org/project/apc-protocol/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/deepfarkade/apc-protocol/ci.yml?branch=main)](https://github.com/deepfarkade/apc-protocol/actions)
[![Docs](https://img.shields.io/badge/docs-online-blue)](docs/documentation.md)

A protocol for decentralized, resilient, and auditable orchestration 
of heterogeneous AI agent ecosystems.

---

APC (Agent Protocol Conductor) is an **open protocol and SDK** designed to orchestrate distributed AI agents in a truly decentralized, resilient, and auditable way. With APC, you can build intelligent systems where multiple agents—each with their own roles and capabilities—work together to accomplish complex tasks, adapt to failures, and recover automatically, all without relying on a central controller.

**🎯 The Problem APC Solves:**
Building multi-agent systems traditionally requires **200+ lines of custom orchestration code**, manual dependency management, custom protocols, and complex error handling for every project.

**⚡ The APC Solution:**
Just **define workflow steps and dependencies** - APC handles everything else automatically! Role-based routing, dependency management, error handling, service discovery, and communication protocols are all built-in.

Key features include:
- **Dynamic Leadership:** Any agent can become the conductor, coordinating workflows and handing off control as needed.
- **Sequenced Task Execution:** Define and manage multi-step processes, with each agent performing specialized subtasks.
- **Checkpointing & Failover:** Progress is saved at every step, so if an agent fails, another can seamlessly take over from the last checkpoint—no lost work, no manual intervention.
- **Interoperability:** Built on Protobuf schemas, APC supports cross-language agent ecosystems (Python, TypeScript, Java, and more).
- **Extensibility & Security:** Easily add new message types, enforce security with mTLS/JWT, and integrate custom business logic or LLMs.

APC is production-ready and ideal for both classic automation and advanced AI-powered workflows. Whether you're building ETL pipelines, LLM chatbots, or autonomous fleets, APC gives you the tools to create robust, scalable, and future-proof agent systems.

---

## 🚀 Quick Start

### 📥 Installation
```sh
# Install from PyPI
pip install apc-protocol

# Or from source
git clone https://github.com/deepfarkade/apc-protocol.git
cd apc-protocol
python setup.py
```

### ⭐ **Try APC in 30 Seconds (No Setup Required!)**
```sh
# Run the simple demo - shows APC benefits immediately
python examples/real_world/apc_simple_demo.py
```

### 🔥 **Most Popular: Real AI Workflow**
```sh
# 1. Add Azure OpenAI key to .env file
# 2. Run 3-agent research workflow
python examples/real_world/simple_azure_openai_demo.py
```

## 🧑‍💻 Basic Usage

```python
from apc import Worker, Conductor
from apc.transport import GRPCTransport

# Create worker with specific roles
worker = Worker("my-worker", roles=["data-processor"])

# Register task handlers
@worker.register_handler("process_data")
async def handle_data(batch_id: str, step_name: str, params: dict):
    # Your processing logic here
    return {"processed": params["data"], "status": "completed"}

# Set up transport and start
transport = GRPCTransport(port=50051)
worker.bind_transport(transport)
await transport.start_server()
```

## 🛠️ Key Features

- **Protobuf-based message schemas** for cross-language interoperability
- **Pluggable checkpoint manager** (in-memory, Redis, S3)
- **State machine engine** for conductor and worker agents
- **gRPC and WebSocket transport adapters**
- **Dynamic Leadership**: Any agent can become the conductor
- **Fault Tolerance**: Automatic failover and recovery
- **Cross-Language Support**: Python, TypeScript, Java, and more
- **Checkpointing**: Save progress and resume from failures
- **Security Ready**: mTLS, JWT authentication support

---

## 🏗️ Architecture Overview

![APC Architecture](docs/images/apc-architecture.png)

APC Protocol enables decentralized agent coordination with:

- **Conductor Agent**: The orchestrator that assigns tasks to Worker Agents based on a workflow plan. Maintains execution state and error recovery logic.
- **Worker Agent**: Domain-specific agents that perform specialized subtasks. They respond to commands from Conductors and return results.
- **gRPC/WebSocket Layer**: Communication backbone that enables bidirectional, low-latency messaging between agents.
- **Checkpoint Store**: Persistent storage layer used to save execution state. Enables seamless recovery without restarting entire workflows.

This modular setup enables dynamic, scalable, and fault-tolerant agent workflows where control is coordinated yet loosely coupled through standardized message passing.

---

## 📚 Examples & Tutorials

### 🎯 **Value-Focused Demonstrations**
**Every example explicitly shows what problems APC solves and why it's essential:**

| Demo | Description | Setup | Best For |
|------|-------------|-------|----------|
| 🎯 [`apc_simple_demo.py`](examples/real_world/apc_simple_demo.py) | Data processing pipeline | ❌ **None needed!** | ⭐ **Start here** - No setup required |
| 🔥 [`simple_azure_openai_demo.py`](examples/real_world/simple_azure_openai_demo.py) | Research → Analysis → Report | ✅ Azure OpenAI | **Most popular** - Real AI workflow |
| ✈️ [`anthropic_travel_planning_demo.py`](examples/real_world/anthropic_travel_planning_demo.py) | Travel planning workflow | ✅ Anthropic Claude | **Claude AI** demonstration |
| 📊 [`gemini_financial_analysis_demo.py`](examples/real_world/gemini_financial_analysis_demo.py) | Financial analysis pipeline | ✅ Google Gemini | **Gemini AI** demonstration |
| 🏭 [`azureopenai_supply_chain_demo.py`](examples/real_world/azureopenai_supply_chain_demo.py) | Supply chain management | ✅ Azure OpenAI | **Business automation** |

### 🎯 **What These Demos Prove**

#### ❌ **WITHOUT APC (Traditional Approach):**
- 💻 **~200+ lines** of custom orchestration code needed
- 🔧 Custom message passing between agents
- ⏰ Manual timeout and error handling  
- 🔄 Complex dependency tracking and execution order
- 🔍 Service discovery and agent registration
- 🛠️ Custom retry logic and failure recovery

#### ✅ **WITH APC (These Examples):**
- ⚡ **~15 lines** to define workflow steps and dependencies
- 🤖 Automatic role-based routing and execution
- 🛡️ Built-in timeout, error handling, and retries
- 📋 Dependency management handled automatically
- 🔍 Service discovery built into the protocol
- ✨ **Just focus on your agent logic - APC handles the rest!**

### 🚀 **Quick Setup for API Demos**

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Add your API keys to `.env`:**
   ```bash
   # For Azure OpenAI demos (automatically detected by APC)
   AZURE_OPENAI_API_KEY=your_key_here
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
   AZURE_OPENAI_API_VERSION=2024-02-15-preview  # Optional
   
   # For Anthropic demos (coming soon)
   ANTHROPIC_API_KEY=your_key_here
   
   # For Gemini demos (coming soon)
   GOOGLE_API_KEY=your_key_here
   ```

3. **Run any demo - APC automatically detects and uses your .env settings!**
   ```bash
   python examples/real_world/simple_azure_openai_demo.py
   ```

### 🗂️ **Checkpoints & Output**

**Checkpoint Management:**
- All workflow state is automatically saved to `./checkpoints/` directory
- Checkpoints enable automatic recovery if conductors or agents fail
- Default checkpoint interval: 30 seconds (configurable)
- Each checkpoint includes full workflow state, timing, and recovery metadata

**Output Files:**
- **Reports:** Generated research reports are saved as `reports/azure_research_report_<batch_id>.txt`
- **Logs:** Colored, structured logging shows workflow progress in terminal
- **Checkpoints:** JSON files in `./checkpoints/` contain complete workflow state

**Project Directory Structure:**
```
./checkpoints/                                 # Workflow checkpoints
├── azure_research_ws_1751380943.json         # WebSocket workflow checkpoint
├── azure_research_1751378779.json            # gRPC workflow checkpoint  
└── batch_<id>_checkpoint.json                # Additional workflow states

./reports/                                     # Generated reports  
├── azure_research_report_ws_1751381636.txt   # Latest research report
├── azure_research_report_1751378779.txt      # Previous reports
└── azure_research_report_<batch_id>.txt      # Additional reports
```

**Log Colors (for easy visual tracking):**
- 🟡 **Yellow (WARNING):** Key workflow events, progress, and results
- 🔴 **Red (ERROR):** Failures and critical issues
- 🔵 **Cyan (DEBUG):** Detailed technical information  
- 🟣 **Magenta (CRITICAL):** System-level failures
- 🟣 **Purple/Violet:** LLM streaming responses and model calls

**LLM Streaming Features:**
- 🎨 **Real-time streaming:** See AI responses as they generate
- 🤖 **Model identification:** Clear display of which AI model is responding
- ⚡ **Agent tracking:** Know which agent is making each LLM call
- 📊 **Performance stats:** Response time and character count displayed

### 📖 **Additional Resources**
- **[Complete Documentation](docs/documentation.md)** - Architecture, message schemas, state machines, checkpointing, transport adapters, security, registry, and advanced LLM integration
- **[Usage Guide](docs/USAGE_GUIDE.md)** - Comprehensive tutorials, production deployment, and advanced examples
- **[Basic Examples](examples/basic/)** - Simple working code to get started
- **[Protocol Specification](proto/apc.proto)** - Technical details and specifications

---

## 🧠 **LLM Integration & Advanced Features**

### 🎨 **Streaming LLM Support**

APC now includes production-ready streaming LLM clients with automatic environment configuration and colored terminal output:

```python
from apc.helpers.llms import AzureOpenAIStreamingClient

# Automatically loads from .env file - no manual configuration needed!
client = AzureOpenAIStreamingClient()

# Real-time streaming with purple/violet colored output
response = client.chat_completion_streaming(
    agent_name="Research Agent",
    messages=[{"role": "user", "content": "Analyze market trends"}],
    max_tokens=500
)
```

### 📁 **Modular LLM Architecture**

All LLM providers are organized in a clean, extensible structure:

```
src/apc/helpers/llms/
├── __init__.py              # Unified exports
├── base.py                  # BaseLLMClient (inherit from this)
├── azure_openai.py          # ✅ Full implementation
├── anthropic.py             # 🚧 Template ready
├── gemini.py                # 🚧 Template ready
├── openai.py                # 🚧 Template ready
└── custom_provider.py       # 🚧 Add your own here
```

### 🔑 **Environment Configuration**

All LLM settings are automatically loaded from your `.env` file:

```bash
# Azure OpenAI (Fully Supported)
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Anthropic (Template Ready)
ANTHROPIC_API_KEY=your_anthropic_api_key_here
ANTHROPIC_MODEL=claude-3-sonnet-20240229

# Google Gemini (Template Ready)
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-pro
```

---

## 🚀 **Example: Multi-Agent Research Workflow with APC**

Here's how APC transforms complex multi-agent coordination:

**🎯 Scenario:** Research → Analysis → Report generation using 3 specialized AI agents

**❌ Traditional Approach (200+ lines):**
```python
# Complex custom orchestration code needed:
# - Agent discovery and registration
# - Custom message passing protocols  
# - Manual dependency tracking
# - Error handling and retries
# - Timeout management
# - Data serialization/deserialization
# - Resource coordination
# ... 200+ lines of boilerplate code
```

**✅ With APC (15 lines):**
```python
# Just define the workflow - APC handles everything!
workflow = conductor.create_workflow("research_workflow")

# Step 1: Research (no dependencies)
workflow.add_step("conduct_research", required_role="researcher")

# Step 2: Analysis (waits for research)  
workflow.add_step("analyze_data", required_role="analyzer", 
                  dependencies=["conduct_research"])

# Step 3: Report (waits for analysis)
workflow.add_step("generate_report", required_role="reporter",
                  dependencies=["analyze_data"])

# Execute - APC orchestrates everything automatically!
result = await conductor.execute_workflow(workflow)
```

**🎯 Result:** APC automatically handles role-based routing, dependency management, error recovery, timeouts, and data flow between agents. No custom orchestration code needed!

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```sh
git clone https://github.com/deepfarkade/apc-protocol.git
cd apc-protocol
python setup.py
python scripts/test_package.py
```

### Key Files
- [`proto/apc.proto`](proto/apc.proto) - Protocol definitions
- [`src/apc/`](src/apc/) - Core Python SDK
- [`examples/`](examples/) - Usage examples
- [`docs/`](docs/) - Documentation

### Testing
```sh
# Run basic tests
python scripts/test_package.py

# Run protocol demo
python scripts/demo.py

# Test example workflows
python examples/real_world/apc_simple_demo.py
python examples/basic/simple_grpc.py
```

---

## 📚 **Advanced Topics & Detailed Comparisons**

For comprehensive technical documentation including:
- **Framework Comparisons**: Detailed comparison with AutoGen and other multi-agent frameworks
- **Protocol Evolution**: Understanding MCP → A2A → ACP → APC evolution
- **Architecture Deep-Dive**: Message schemas, state machines, transport adapters
- **Real-World Scenarios**: Complex deployment patterns and use cases
- **Security & Production**: mTLS, JWT, policy engines, enterprise deployment

See our complete documentation:
- **[Technical Documentation](docs/documentation.md)** - Complete architecture and advanced features
- **[Usage Guide](docs/USAGE_GUIDE.md)** - Comprehensive tutorials and production patterns

---

---

## 📦 Release Information

- **Current Release:** v0.1.x (Alpha)
- See [Releases](https://github.com/deepfarkade/apc-protocol/releases) for changelogs and version history.
- This is the first public alpha release of the APC protocol and SDK.

---

## 🛡️ License
MIT


