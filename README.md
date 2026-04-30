# 🚀 Distributed Load Balancing System for LLM Inference

A high-performance distributed system that efficiently balances Large Language Model (LLM) inference requests across multiple GPU workers using round-robin scheduling, with integrated Retrieval-Augmented Generation (RAG) capabilities.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Performance Metrics](#performance-metrics)
- [How It Works](#how-it-works)

## 🎯 Overview

This project implements a distributed load balancing system designed to handle concurrent LLM inference requests efficiently. It distributes workload across multiple GPU workers using a round-robin algorithm, integrates RAG for context-enhanced responses, and provides comprehensive performance metrics.

**Key Use Cases:**
- High-throughput LLM inference serving
- Distributed AI workload management
- Load testing LLM systems
- RAG-enhanced question answering at scale

## 🏗️ Architecture

```
┌─────────────┐
│   Client    │
│Load Generator│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Master    │
│  Scheduler  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Load     │
│  Balancer   │
└──────┬──────┘
       │
       ├──────────┬──────────┬──────────┐
       ▼          ▼          ▼          ▼
   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
   │Worker 0│ │Worker 1│ │Worker 2│ │Worker 3│
   └────┬───┘ └────┬───┘ └────┬───┘ └────┬───┘
        │          │          │          │
        └──────────┴──────────┴──────────┘
                      │
                      ▼
              ┌──────────────┐
              │  RAG System  │
              │  + LLM API   │
              └──────────────┘
```

### Components

| Component | Description |
|-----------|-------------|
| **Load Balancer** | Implements round-robin distribution across GPU workers |
| **Master Scheduler** | Coordinates request routing and worker allocation |
| **GPU Workers** | Process LLM inference tasks with RAG context retrieval |
| **RAG System** | Retrieves relevant context from knowledge base |
| **LLM Inference** | Integrates with Ollama API for text generation |
| **Load Generator** | Simulates concurrent users with ThreadPoolExecutor |

## ✨ Features

- ⚡ **Round-Robin Load Balancing**: Evenly distributes requests across workers
- 🔄 **Concurrent Request Handling**: Multi-threaded load generation with configurable thread pools
- 🧠 **RAG Integration**: Context-enhanced responses using retrieval system
- 📊 **Performance Metrics**: Real-time latency, throughput, and worker distribution tracking
- 🎛️ **Dual Operating Modes**: 
  - **Normal Mode**: Minimal processing for latency testing
  - **Stress Mode**: Full RAG + LLM inference for load testing
- 🔧 **Configurable Parameters**: Adjustable workers, users, and thread limits
- 🤖 **Ollama Integration**: Uses lightweight `smollm:135m` model

## 📦 Prerequisites

- **Python**: 3.8 or higher
- **Ollama**: Installed and running locally
  ```bash
  # Install Ollama from https://ollama.ai
  # Pull the model
  ollama pull smollm:135m
  
  # Start Ollama server (runs on http://localhost:11434)
  ollama serve
  ```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/OmarH-creator/Distributed_Load_Balancing.git
   cd Distributed_Load_Balancing
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Ollama is running**
   ```bash
   curl http://localhost:11434/api/generate -d '{"model":"smollm:135m","prompt":"test"}'
   ```

## ⚙️ Configuration

Edit `common/config.py` to customize system behavior:

```python
MODE = "stress"        # "normal" or "stress"
NUM_USERS = 1000       # Number of concurrent requests
NUM_WORKERS = 4        # Number of GPU workers
MAX_THREADS = 16       # Maximum concurrent threads
```

### Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `MODE` | Operating mode (`normal` or `stress`) | `stress` |
| `NUM_USERS` | Total number of requests to generate | `1000` |
| `NUM_WORKERS` | Number of worker instances | `4` |
| `MAX_THREADS` | Maximum concurrent threads | `16` |

### Operating Modes

- **Normal Mode**: Sends minimal prompts (`.`) with 1-token responses for latency benchmarking
- **Stress Mode**: Full RAG retrieval + LLM inference with 10-token responses for load testing

## 🚀 Usage

### Run the Complete System

```bash
python main.py
```

### Expected Output

```
Starting project test...
Mode: stress
Users: 1000
Workers: 4
----------------------------------------
Processing requests: 100%|████████████| 1000/1000 [00:45<00:00, 22.15it/s]

FINAL RESULTS
----------------------------------------
Mode: stress
Total requests: 1000
Workers used: 4
Total time: 45.12s
Average latency: 0.18s
Throughput: 22.16 requests/second

WORKER DISTRIBUTION
----------------------------------------
Worker 0: 250 requests
Worker 1: 250 requests
Worker 2: 250 requests
Worker 3: 250 requests

SAMPLE ANSWER
----------------------------------------
Load balancing distributes requests across multiple worker nodes to improve performance.
```

## 📁 Project Structure

```
llm-load-balancing-project/
├── main.py                      # Entry point and metrics aggregation
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
│
├── common/                      # Shared utilities
│   ├── config.py               # System configuration
│   └── models.py               # Data models (Request, Response)
│
├── lb/                         # Load balancing
│   └── load_balancer.py        # Round-robin load balancer
│
├── master/                     # Coordination
│   └── scheduler.py            # Master scheduler
│
├── workers/                    # Worker pool
│   ├── __init__.py            # Module initialization
│   └── gpu_worker.py          # GPU worker implementation
│
├── client/                     # Load generation
│   └── load_generator.py      # Concurrent request generator
│
├── llm/                        # LLM integration
│   └── inference.py           # Ollama API interface
│
└── rag/                        # RAG system
    ├── retriever.py           # Context retrieval
    └── knowledge_base.txt     # Knowledge base content
```

## 📊 Performance Metrics

The system tracks and reports:

- **Total Requests**: Number of requests processed
- **Total Time**: End-to-end execution time
- **Average Latency**: Mean request processing time
- **Throughput**: Requests per second
- **Worker Distribution**: Request count per worker (validates load balancing)

### Sample Performance

| Configuration | Throughput | Avg Latency | Workers |
|---------------|------------|-------------|---------|
| 1000 users, 4 workers, 16 threads | ~22 req/s | ~0.18s | 4 |
| 500 users, 2 workers, 8 threads | ~18 req/s | ~0.11s | 2 |

## 🔍 How It Works

### Request Flow

1. **Load Generator** creates `NUM_USERS` concurrent requests using ThreadPoolExecutor
2. **Master Scheduler** receives each request and forwards to Load Balancer
3. **Load Balancer** selects next worker using round-robin algorithm
4. **GPU Worker** processes request:
   - Calls RAG retriever for context (stress mode)
   - Sends prompt + context to Ollama API
   - Returns response with latency metrics
5. **Main** aggregates results and displays performance metrics

### Load Balancing Algorithm

```python
def get_worker(self):
    worker = self.workers[self.index]
    self.index = (self.index + 1) % len(self.workers)
    return worker
```

Simple round-robin ensures even distribution across workers.

### RAG Integration

In stress mode, each request:
1. Retrieves relevant context from knowledge base
2. Constructs prompt: `Context: {context}\nQuestion: {query}\nAnswer in one short sentence:`
3. Sends to LLM for inference

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- Additional load balancing strategies (least connections, weighted)
- Fault tolerance and worker health checks
- Real-time monitoring dashboard
- Support for multiple LLM backends
- Advanced RAG with vector embeddings

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Omar Hassan**
- GitHub: [@OmarH-creator](https://github.com/OmarH-creator)

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for local LLM inference
- Built for distributed systems and load balancing research
