# FastAPI Boilerplate

## Overview

This FastAPI Boilerplate project implements a scalable asynchronous FastAPI backend for a messenger application with PostgreSQL DBMS, SQLAlchemy ORM and Alembic migrations. New users can be created and authenticated via OAuth JWT Bearer authentication flow with basic scopes. Authenticated users can create new multi-user message threads and send/receive messages to/from other users. Users with admin scopes are able to list and update other users.

Project's architecture can easily be adapted and extended to any FastAPI application in very short time.

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

To apply alembic migrations configure database credentials inside .envs files and "upgrade" the database by running:

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

If launched successfully Swagger UI documentation should become available at: `http://localhost:8080/docs`

API endpoints can be interacted with via `http://localhost:8080/api/` URLs.

## Files Overview 

API implementation can be found inside /messenger:

- /messenger/core - Core app functionality, including all of the base classes (e.g. base database controller and repository).
- /messenger/app/ - App logic with specific class implementations (e.g. User database controller and repository).
- /messenger/routers/ - FastAPI API routers with all of the API endpoints.

- /alembic - Alembic configuration files and migration files.

- /compose/production/messenger - Production Docker files with entrypoint and start command scripts.  

## Architecture Overview 

The backend implements a variation of an MVC architecture:

- SQLAlchemy ORM models represent various data structures (e.g. users and messages).
- FastAPI Routers act as the main client API interface (i.e. views).
- Database Controllers implement high-level data business logic.
- Database Controller Services implement high-level cross-controller data business logic.
- Database Repositories handle low-level data access and operations.

## ORM Models Overview 

Three SQLAlchemy ORM models have been implemented to represent: Users, Messages and Threads.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.
