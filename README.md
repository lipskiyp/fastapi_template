# FastAPI Messenger Back-End 

## Overview

The project implements a scalable asynchronous FastAPI backend for a messenger application with OAuth JWT Bearer user authentication flow. New users can be created and authenticated via the API. Authenticated users can create new multi-user message threads and send/receive messages to/from other users. 

The project architecture can easily be modified and extended for any other REST API service.

## Core Technologies

- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker 
- Jose

## Requirements

PostgreSQL, Docker and Docker Compose (unless launched locally) are necessary to run the application and need to be installed on the machine before launch.

If launched locally, specific library requirements can be installed using your preferred package manager, e.g. pip:

```bash
pip3 install -r requirements.txt
```

Configs can be updated inside .envs files with the desired application configurations, database credentials etc.

## Alembic Migrations

To apply alembic SQLAlchemy migrations to the database configure the database credentials inside .envs files and then run:

```bash
alembic upgrade head
```

## Launch

### Locally:

```bash
python main.py
```

### Docker:

```bash
docker compose -f launch.yml up
```

NB Ensure POSTGRESQL_HOST=host.docker.internal in ./envs/.production/.messenger if PostgreSQL is running on localhost.

If launched successfully SwaggerUI documentation should become available at: `http://localhost:8080/docs`

## Files Overview 

API implementation can be found inside /messenger:

- Core app functionality, including all of the base classes (e.g. base database controller and repository), can be found in /messenger/core.
- Main app logic can be found in /messenger/app/.
- FastAPI API routers, including all of the API endpoints, can be found in /messenger/routers/.

## Architecture Overview 

The backend implements a variation of an MVC architecture:

- Models represent various data structures (e.g. users and messages).
- Routers act as API client interfaces (i.e. views).
- Controllers implement high-level data business logic.
- Controller Services implement high-level cross-controller data business logic.
- Repositories handle low-level data access and operations.

## ORM Models Overview 

Three SQLAlchemy ORM models have been implemented to represent: User, Message and Thread.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.
