# FastAPI Messenger Back-End 

## Overview

The project implements scalable asynchronous FastAPI backend for a messenger application.   

## Core Technologies

- FastAPI
- FastAPI Filters
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker 

## Requirements

PostgreSQL, Docker and Docker Compose are all necessary to run the application and need to be installed on the machine before launch.

Ensure .envs files are correctly setup with the desired application configurations and appropriate database credentials etc.

## Launch

```bash
python main.py
```

## ORM Overview 

Three SQLAlchemy ORM models have been implemented to represent: User, Message and Thread.

- User and Thread have many-to-many relationship expressed via users_and_threads association table.
- User and Message have one-to-many relationship.
- Thread and Message have one-to-many relationship.







1. Base exception + Integrity error
2. Docker
3. Alembic 
4. messages + threads 
5. auth? 
6. PyTests 
7. Redis cache
