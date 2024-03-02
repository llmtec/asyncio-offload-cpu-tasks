# Asyncio: efficiently and safely offloading CPU-bound tasks to shared executors

This project demonstrates how to integrate Python's concurrent futures executors with FastAPI for managing background tasks efficiently.

Please see our full blogpost here: https://www.llmtec.com/asyncio-offload-cpu-bound-tasks-safely

## Overview

The application showcases the use of a shared `ThreadPoolExecutor` or `ProcessPoolExecutor` to offload CPU-intensive or I/O-bound tasks, keeping the FastAPI application responsive and scalable.

## Structure

- `main.py`: The FastAPI application entry point.
- `executor.py`: Defines the `AppExecutor` class for managing a shared executor instance.

## Requirements

Python 3.7+ is required. All dependencies are listed in `requirements.txt`.

## Setup

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

This command starts a local server. By default, you can visit the application at `http://127.0.0.1:8000`.

## Usage

Visit the root endpoint (`/`) to execute a simple task in the background using the shared executor.

## License

This project is open-sourced under the MIT license.

