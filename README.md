# FastAPI Boilerplate

Production-ready scalable asynchronous FastAPI backend template. 

## Overview

The aim of the project was to implement a scalable production-ready FastAPI template with out-of-the-box support for a number of common features: asynchronous support, CRUD database controllers/repositories, PostgreSQL DBMS, SQLAlchemy ORM, Alembic migrations, Docker containerization, Pydantic type validation, basic user authorization and authentication with permission scopes. Project's core logic, including the base class implementations is isolated within the /core directory, while the application specific logic can be found inside the /app directory. 

An example implementation for a messenger application can be found inside the /app directory. The app allows users to be created, authenticated and authorized via OAuth JWT Bearer authentication flow with basic access scopes (regular, admin and superuser). Authenticated users can create new multi-user message threads and send/receive messages to/from other users. Users with admin scopes are able to list and update other users.

Project's layered architecture can easily be adapted and extended to any FastAPI service with very little effort.

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

NB If PostgreSQL is running on localhost and the project is launched inside Docker ensure POSTGRESQL_HOST=host.docker.internal inside .envs files (./envs/.production/.messenger).

If launched successfully Swagger UI documentation should become available at: `http://localhost:8080/docs`

API endpoints can be interacted with via `http://localhost:8080/api/` URLs.

## Files 

- /.envs - Environment variables.
- /alembic - Alembic configuration and migration files.
- /compose - Dockerfile, entrypoint and start command scripts.  
- /configs - Pydantic app configuration settings for the app, authentication and database.
- /core - Core functionality, including the base class implementations (e.g. base database controller and repository).
- /app - Application specific logic with concrete class implementations (e.g. User database controller and repository).
- /routers - FastAPI API routers with all of the API endpoints.

## Architecture 

The backend implements a layered architecture that combines multiple functional layers:

- SQLAlchemy ORM Model layer implements the data structures (e.g. users and messages).
- FastAPI Router layer acts as the main client interface for the API (i.e. views).
- Database Controllers layer handles high-level data business logic.
- Database Controller Services layer handles high-level cross-controller data business logic.
- Database Repositories layer handles low-level data access and operations.

## Models 

Three SQLAlchemy ORM models have been implemented to represent: Users, Messages and Threads.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.

All models are derived from a CommonBase that implements four default columns: id, created_at, updated_at and deleted (for soft deletes).

## Authentication

// TO DO DESCRIPTION
