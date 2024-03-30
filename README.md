# FastAPI Boilerplate

## Overview

This boilerplate project implements a scalable production-ready FastAPI backend template that supports a number of features out of the box: asynchronous support, PostgreSQL DBMS, SQLAlchemy ORM, Alembic migrations, Docker containerization, Pydantic type validation, basic user authorization and authentication with permission scopes. Project's core logic, including the base class implementations is isolated within the core directory, while the application specific logic can be found inside the app directory. 

An example backend for a messenging app was implemented inside the app directory. New users can be created and authenticated via OAuth JWT Bearer authentication flow with basic access scopes (regular, admin and superuser). Authenticated users can create new multi-user message threads and send/receive messages to/from other users. Users with admin scopes are able to list and update other users.

Project's layered architecture can be easily adapted and extended to any FastAPI service with very little effort.

## Technologies

- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker 
- Jose

## Requirements

Docker, Docker Compose (unless launched locally) and PostgreSQL are necessary to run the application and need to be installed on the machine before launch.

If launched locally, specific library requirements can be installed using your preferred package manager, e.g. pip:

```bash
pip3 install -r requirements.txt
```

Configs can be updated inside .envs files with the desired application configurations, database credentials etc.

## Migrations

To apply alembic migrations configure the database credentials inside .envs files and "upgrade" the database by running the following command inside project's directory:

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

NB If PostgreSQL is running on localhost and the project us launched inside Docker ensure POSTGRESQL_HOST=host.docker.internal inside .envs files (./envs/.production/.messenger).

If launched successfully Swagger UI documentation should become available at: `http://localhost:8080/docs`

API endpoints can be interacted with via `http://localhost:8080/api/` URLs.

## Files 

- /.envs - Environment variables.
- /alembic - Alembic configuration and migration files.
- /compose - Dockerfile as well as entrypoint and start command scripts.  
- /configs - Pydantic app configuration settings for the app, authentication and database.
- /core - Core app functionality, including all of the base classes (e.g. base database controller and repository).
- /app/ - Specific service logic with concrete class implementations (e.g. User database controller and repository).
- /routers/ - FastAPI API routers with all of the API endpoints.

## Architecture 

The backend implements a layered architecture that combines multiple functional layers:

- SQLAlchemy ORM model layer represent various data structures (e.g. users and messages).
- FastAPI Routers layer acts as the main client interface for the API (i.e. views).
- Database Controllers layer implements high-level data business logic.
- Database Controller Services layer implements high-level cross-controller data business logic.
- Database Repositories layer handles low-level data access and operations.

## Models 

Three SQLAlchemy ORM models have been implemented to represent: Users, Messages and Threads.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.

All models are derived from a CommonBase that implements four default columns: id, created_at, updated_at and deleted (for soft deletes).

## Authentication

// TO DO
