# My FastAPI Application
This repository contains a FastAPI application that is containerized with Docker and uses a Conda environment for managing dependencies. The application provides a simple REST API to demonstrate the functionality.

## Prerequisites
Before you begin, ensure you have the following installed on your system:

- Docker
- Conda (optional, needed only for local development outside Docker)

## Project Structure
The project files are organized as follows:

```
my_fastapi_app/
│
├── app/
│   ├── __init__.py             # Makes app a Python module
│   ├── main.py                 # FastAPI application entry point
│   ├── model.py                # ML model wrapper
│   └── trained-model-0.1.0.pkl # pickled model
│
├── Dockerfile                  # Dockerfile for building the application container
├── environment.yml             # Conda environment file
└── README.md                   # This file
```

## Setup and Installation
### Local Setup (Optional)
If you prefer to run the application locally (without Docker), follow these steps:

1. Create and activate the Conda environment:
```
conda env create -f environment.yml
conda activate testenv
```
2. Run the application:
```
uvicorn app.main:app --reload
```

### Using Docker
To run the application in a Docker container, follow these steps:

1. Build the Docker image:
```
docker build -t fastapi-test .
```
2. Run the Docker container:
```
docker run -p 8000:8000 fastapi-test
```

## Accessing the Application
Once the application is running, you can access it via:

Localhost URL: http://localhost:8000
API Documentation: http://localhost:8000/docs
The API documentation page provides an interactive UI to test the API endpoints.

## Deployment
The application can be deployed on any Docker-supported platform. Ensure that the port 8000 is open on the host machine or remapped appropriately when running the Docker container.