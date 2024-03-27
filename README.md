# FastAPI Boilerplate

## Overview

This FastAPI boilerplate project implements a scalable asynchronous FastAPI backend for a messenging service with PostgreSQL DBMS, SQLAlchemy ORM, Alembic migrations, Docker containerization and Pydantic type validation. New users can be created and authenticated via OAuth JWT Bearer authentication flow with basic access scopes (regular, admin and superuser). Authenticated users can create new multi-user message threads and send/receive messages to/from other users. Users with admin scopes are able to list and update other users as well as access all threads.

Project's architecture can be easily adapted and extended to any FastAPI service with very little effort.

## Technologies

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

API implementation can be found inside /messenger:

- /messenger/core - Core app functionality, including all of the base classes (e.g. base database controller and repository).
- /messenger/app/ - Specific service logic with concrete class implementations (e.g. User database controller and repository).
- /messenger/routers/ - FastAPI API routers with all of the API endpoints.

- /alembic - Alembic configuration files and migration files.

- /compose/production/messenger - Production Docker files with entrypoint and start command scripts.  

## Architecture 

The backend implements a variation of an MVC architecture:

- SQLAlchemy ORM models represent various data structures (e.g. users and messages).
- FastAPI Routers act as the main client interface to interact with the API (i.e. views).
- Database Controllers implement high-level data business logic.
- Database Controller Services implement high-level cross-controller data business logic.
- Database Repositories handle low-level data access and operations.

## Models 

Three SQLAlchemy ORM models have been implemented to represent: Users, Messages and Threads.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.

The Base ORM model implements four default columns: id, created_at, updated_at and deleted (for soft deletes).

## Authentication

// TO DO
