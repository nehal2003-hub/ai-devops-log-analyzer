# AI-Powered DevOps Log Analyzer

## Project Overview

The AI-Powered DevOps Log Analyzer is a Python-based application that analyzes application log files and uses a locally running AI model to provide troubleshooting recommendations.

It identifies log levels such as INFO, WARNING, ERROR, and CRITICAL, extracts important errors, and sends them to an AI model for analysis.

## Features

- Reads application logs from a log file.
- Counts INFO, WARNING, ERROR, and CRITICAL messages.
- Detects and extracts ERROR and CRITICAL entries.
- Uses Ollama with the Llama 3.2 1B model for AI-powered log analysis.
- Generates possible causes and troubleshooting recommendations.
- Runs inside a Docker container.

## Technologies Used

- Python
- Docker
- Ollama
- Llama 3.2 1B
- REST API
- Requests library

## Project Structure

```text
ai-devops-log-analyzer/
├── analyzer/
│   └── log_analyzer.py
├── logs/
│   └── app.log
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

- Windows, Linux, or macOS
- Python (for running outside Docker)
- Docker Desktop
- Ollama
- Llama 3.2 1B model

## Setup

### 1. Install Ollama

Download Ollama from:

https://ollama.com/

Download the AI model:

```bash
ollama pull llama3.2:1b
```

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-devops-log-analyzer.git
cd ai-devops-log-analyzer
```

### 3. Build the Docker image

```bash
docker build -t ai-devops-log-analyzer .
```

### 4. Run the application

Make sure Docker Desktop and the Ollama service are running.

```bash
docker run --rm ai-devops-log-analyzer
```

## How It Works

1. The application reads the sample application log file.
2. It counts messages by severity level.
3. It extracts ERROR and CRITICAL messages.
4. It sends the detected errors to the local Ollama API.
5. The Llama 3.2 model analyzes the errors.
6. The application displays possible causes and troubleshooting recommendations.

## Sample Log Issues

The sample log file includes:

- High memory usage warning
- Database connection failure
- Connection timeout
- Application service crash

## Learning Outcomes

Through this project, I practiced:

- Python automation and log processing
- Docker image creation and container execution
- REST API integration
- Running local AI models with Ollama
- Applying AI to a practical DevOps troubleshooting use case

## Author

Nehal Shetty

