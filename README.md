# TestWork Project

## Description

This FastAPI application provides an API for interacting with a database. 
The main functionality includes retrieving all records from the database sorted 
by their increasing IDs.

## Installation

First of all, clone the project repository:

```bash
git clone git@github.com:RoostiqueTheMan/TestWork.git
```

Go to directory with project

## Running the Application with Docker Compose

To run the application using Docker Compose, ensure you have Docker 
and Docker Compose installed on your machine. Follow these steps:

1. Build and start the Docker containers:

```bash
    docker compose up --build
```
    
2. The application will be available at: [http://127.0.0.1:1477](http://127.0.0.1:1477).

3. To stop the containers, run:
    
```bash
    docker compose down
``` 

## API Documentation

Once the application is running, you can access the interactive API 
documentation at the following URLs:

- Swagger UI: [http://172.20.0.8:1477/docs](http://172.20.0.8:1477/docs)
- ReDoc: [http://172.20.0.8:1477/redoc](http://172.20.0.8:1477/redoc)
- Health check: http://172.20.0.8:1477/ping
- To get all records from the database, use the following 
endpoint:: http://172.20.0.8:1477/get-all
 
## Modules

The application contains the following main modules:
- dbase-service: module with postgresql script
- api-service: main api service

## Testing

For testing the application, use `pytest`. Ensure all dependencies are 
installed and run the following command to execute tests:

```bash
pytest
```
