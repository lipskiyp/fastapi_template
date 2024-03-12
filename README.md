# FastAPI Messenger Back-End 

## Overview

The project implements a scalable asynchronous FastAPI backend for a messenger application with OAuth JWT Bearer user authentication flow. The project architecture can easily be modified and utilized for any other REST API. New users can be created and authenticated via the API. Authenticated users can create new multi-user message threads and send/receive messages to/from other users. 

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

## Files Overview 

API implementation can be found inside /messenger:

- Core app functionality, including all of the base classes (e.g. base database controller and repository), can be found in /messenger/core.
- Main app logic can be found in /messenger/app/.
- FastAPI API routers, including all of the API endpoints, can be found in /messenger/routers/.

## Architecture Overview 

The backend implements a variation of an MVC architecture:

- Models represent various data structures (e.g. users).
- Routers act as API client interfaces (i.e. views).
- Controllers implement high-level data business logic.
- Controller Services implement high-level cross-controller data business logic.
- Repositories handle low-level data access and operations.

## ORM Models Overview 

Three SQLAlchemy ORM models have been implemented to represent: User, Message and Thread.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.


## In Progress

1. Docker
2. Alembic 
3. Permission groups
