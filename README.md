# Multi-LLM Gateway

A **Multi-LLM Gateway** built with **Python and FastAPI** that provides a single API interface for interacting with multiple Large Language Models (LLMs). The gateway acts as an intermediate layer between the application and different LLM providers, allowing requests to be routed, executed, and managed through one centralized backend.

The main goal of this project is to demonstrate how multiple LLM services can be integrated into a single system using **asynchronous programming, routing logic, service abstraction, and API-based architecture**.

## 🚀 Project Overview

Normally, an application may need to communicate with different LLM providers separately.

For example:

```text
Application
   ├──→ LLM Provider 1
   ├──→ LLM Provider 2
   └──→ LLM Provider 3
```

With a Multi-LLM Gateway, the application communicates with only one backend:

```text
                  ┌──→ LLM 1
                  │
Application → Multi-LLM Gateway ──→ LLM 2
                  │
                  └──→ LLM 3
```

The gateway receives the user's request, determines which model or models should handle it, sends the request to the required LLM services, and returns the response to the client.

## 🛠️ Technologies Used

* **Python** – Core programming language
* **FastAPI** – Backend API framework
* **Asyncio** – Asynchronous execution
* **Pydantic** – Request and response validation
* **LLM APIs** – Communication with external language models
* **Uvicorn** – ASGI server
* **Environment Variables** – Secure API configuration

## 📁 Project Structure

```text
MultiLLM-Gateway/
│
├── README.md
├── config.py
├── main.py
├── router_logic.py
├── routes.py
├── schemas.py
├── services.py
├── test.py
└── testing.py
```

The project uses a modular architecture where API routes, routing decisions, configuration, schemas, and LLM service communication are separated into different files.

## 📌 File Responsibilities

### `main.py`

The main entry point of the FastAPI application.

It creates the FastAPI application and connects the required routes.

The application can be started using:

```bash
uvicorn main:app --reload
```

### `config.py`

Contains configuration-related information used by the application.

This file can be used to manage settings such as:

* API configuration
* Model configuration
* Environment variables
* LLM provider settings

Sensitive API keys should be stored in environment variables instead of directly inside the source code.

### `routes.py`

Contains the API endpoints exposed by the gateway.

The routes receive requests from clients and forward them to the appropriate application logic.

The basic flow is:

```text
Client Request
      ↓
FastAPI Route
      ↓
Router Logic
      ↓
LLM Service
      ↓
Response
```

### `router_logic.py`

Contains the main routing logic of the gateway.

This component determines how incoming requests should be handled.

For example, a request can be routed to a particular LLM based on:

* Selected model
* Request type
* Availability
* Routing configuration
* Application requirements

This separates the routing decision from the API layer.

### `schemas.py`

Contains Pydantic schemas used for validating incoming requests and formatting responses.

For example:

```text
Client
  ↓
JSON Request
  ↓
Pydantic Schema
  ↓
Validated Data
```

This helps ensure that the API receives data in the expected format.

### `services.py`

Contains the logic responsible for communicating with the LLM services.

Instead of putting API calls directly inside the FastAPI routes, the LLM communication is separated into a service layer.

This makes the project easier to maintain and extend.

For example:

```text
Route
  ↓
Service
  ↓
LLM API
  ↓
Response
```

## ⚡ Asynchronous LLM Execution

One of the important concepts demonstrated by this project is **asynchronous programming** using Python's `asyncio`.

When multiple LLMs need to be called, executing them one after another can increase the total response time.

### Sequential Execution

```text
LLM 1 → Wait → LLM 2 → Wait → LLM 3
```

The total time can become large because each request waits for the previous request.

### Parallel Execution

Using asynchronous tasks:

```text
             ┌──→ LLM 1
             │
Request ─────┼──→ LLM 2
             │
             └──→ LLM 3

             ↓
        Collect Results
```

Multiple requests can be started without waiting for each one to finish before starting the next.

This can significantly improve the efficiency of a multi-model gateway.

## 🔄 Request Workflow

The overall workflow is:

### 1. Client Sends Request

A client sends a request to the FastAPI gateway.

```json
{
  "prompt": "Explain artificial intelligence"
}
```

### 2. API Validation

The request is validated using the schemas defined in `schemas.py`.

### 3. Routing Decision

The gateway uses `router_logic.py` to determine which LLM or LLMs should process the request.

### 4. LLM Requests

The service layer sends the prompt to the selected LLM APIs.

If multiple models are configured, the gateway can execute requests asynchronously.

### 5. Collect Responses

The gateway waits for the required responses and collects the results.

### 6. Return Response

The final result is returned to the client through the FastAPI endpoint.

```text
Client
  ↓
FastAPI
  ↓
Schema Validation
  ↓
Router Logic
  ↓
LLM Services
  ↓
LLM Responses
  ↓
Gateway Response
```

## ⏱️ Timeout Handling

An important feature of a multi-LLM system is handling slow or unavailable providers.

For example:

```text
LLM 1 → Response in 2 seconds
LLM 2 → Response in 3 seconds
LLM 3 → Slow / Timeout
```

Instead of allowing the entire application to wait indefinitely, asynchronous timeout handling can be used.

This allows the gateway to continue operating even when one LLM provider is slow or unavailable.

## 🧠 Why Use a Multi-LLM Gateway?

Using a gateway provides several advantages.

### Single API Interface

Applications only need to communicate with one backend instead of integrating every LLM provider individually.

### Model Flexibility

Different models can be selected depending on the requirement.

### Easier Integration

Adding another LLM provider can be handled inside the gateway without requiring major changes to the client application.

### Better Performance

Asynchronous execution allows multiple LLM requests to run concurrently.

### Centralized Management

Routing, configuration, error handling, and LLM communication can be managed from one location.

## 🧪 Testing

The project contains testing files such as:

```text
test.py
testing.py
```

These files can be used to test the gateway functionality, API behavior, and LLM responses.

The FastAPI Swagger interface can also be used to test available endpoints.

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/chandrakiran-1/MultiLLM-Gateway.git
cd MultiLLM-Gateway
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not included, install the dependencies used by the project and create one using:

```bash
pip freeze > requirements.txt
```

## 🔐 Environment Variables

API keys should be stored securely using environment variables.

Example:

```env
LLM_API_KEY=your_api_key
```

Do not commit API keys or other secrets to GitHub.

Add sensitive files to `.gitignore`:

```text
.env
venv/
__pycache__/
```

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Key Features

* Multi-LLM integration
* Single API gateway
* FastAPI backend
* Modular architecture
* LLM routing logic
* Asynchronous execution
* Concurrent LLM requests
* Timeout handling
* Request validation
* Centralized configuration
* Service abstraction
* API testing
* Swagger documentation

## 🔮 Future Improvements

The gateway can be extended with additional production-level features such as:

* Automatic model selection
* Load balancing
* Retry mechanisms
* Fallback models
* Rate limiting
* Authentication
* Request logging
* Response caching
* Cost tracking
* Model performance monitoring
* Provider health checks
* Streaming responses
* Docker deployment
* AWS deployment
* CI/CD integration

## 👨‍💻 Author

**Chandrakiran Reddy**

This project demonstrates practical knowledge of **LLM integration, FastAPI backend development, asynchronous programming, API architecture, routing, service abstraction, and multi-model AI systems**.
