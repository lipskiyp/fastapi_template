# FastAPI Messenger Back-End 

## Overview

The project implements a scalable asynchronous FastAPI backend for a messenger application with OAuth JWT Bearer user authentication flow. 

New users can be created and authenticated via the API. Authenticated users can create new multi-user message threads and send/receive messages to/from other users. 

The backend implements a variation of an MVC architecture:

- Models represent various data structures (e.g. users).
- Routers act as API client interfaces (i.e. views).
- Controllers implement high-level data business logic.
- Repositories handle low-level data access and operations.

## Core Technologies

- FastAPI
- FastAPI Filters
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker 
- Jose

## Requirements

PostgreSQL, Docker and Docker Compose are all necessary to run the application and need to be installed on the machine before launch.

Specific library requirements can be installed using your preferred package manager, e.g. pip:

```bash
pip3 install -r requirements.txt
```

Ensure .envs files are correctly setup with the desired application configurations and appropriate database credentials etc.

## Launch

```bash
python main.py
```

If launched successfully SwaggerUI documentation should become available at: `http://localhost:8080/docs`

## ORM Models Overview 

Three SQLAlchemy ORM models have been implemented to represent: User, Message and Thread.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.


## In Progress

1. Docker
2. Alembic 
3. messages + threads logic
4. Redis cache
