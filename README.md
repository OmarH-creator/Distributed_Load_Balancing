# LLM Load Balancing Project

A distributed load balancing system for Large Language Model inference with GPU workers, RAG capabilities, and fault tolerance.

## Architecture

- **Load Balancer**: Distributes incoming requests across GPU workers using various strategies
- **Master Scheduler**: Coordinates worker allocation and task scheduling
- **GPU Workers**: Execute LLM inference tasks
- **RAG System**: Retrieval-Augmented Generation for enhanced responses
- **Monitoring**: Real-time metrics collection and performance tracking
- **Fault Tolerance**: Automatic failure detection and recovery

## Features

- Multiple load balancing strategies (Round Robin, Least Connections, Weighted)
- GPU resource management
- RAG-enhanced inference
- Real-time monitoring and metrics
- Fault tolerance and automatic recovery
- Configurable worker pools

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run Complete System
```bash
python main.py --mode all --workers 3
```

### Run Individual Components
```bash
# Master scheduler only
python main.py --mode master

# Worker only
python main.py --mode worker

# Client load generator
python main.py --mode client
```

## Configuration

Edit `common/config.py` to customize:
- Worker pool size
- Load balancing strategy
- Model parameters
- Timeout settings

## Results

Performance metrics are saved to the `results/` directory:
- `latency_results.csv`: Request latency data
- `throughput_results.csv`: System throughput metrics
- `test_summary.txt`: Overall test summary

## Project Structure

```
llm-load-balancing-project/
├── main.py                 # Entry point
├── common/                 # Shared utilities
├── client/                 # Load generator
├── lb/                     # Load balancer
├── master/                 # Master scheduler
├── workers/                # GPU workers
├── rag/                    # RAG system
├── llm/                    # LLM inference
├── monitoring/             # Metrics collection
├── fault_tolerance/        # Failure management
└── results/                # Output data
```
