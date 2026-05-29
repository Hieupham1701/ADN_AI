# Genomic Risk Pipeline

An end-to-end service scaffold for processing VCF files, matching variants with ClinVar, calculating genomic risk, and generating reports to predict the disease.

## Overview

This project is structured as a modular backend system:

- FastAPI for API endpoints
- Pipeline modules for variant processing
- Service layer for business logic and report generation
- Celery workers for asynchronous heavy jobs
- Test suite for parser, scoring, and API behavior

## Project Structure

```text
genomic-risk-pipeline/
├── app/
│   ├── api/                    # FastAPI routes and dependencies
│   ├── core/                   # Settings and logging
│   ├── pipeline/               # Main genomic processing pipeline
│   ├── services/               # Business logic and AI explainer
│   ├── models/                 # Database models
│   ├── schemas/                # Pydantic schemas
│   └── main.py                 # FastAPI entrypoint
├── workers/                    # Celery worker and tasks
├── data/                       # ClinVar and other local datasets
├── scripts/                    # Utility CLI scripts
├── tests/                      # Unit and API tests
├── docker/                     # Dockerfile and compose setup
├── notebooks/                  # Research and analysis notebooks
├── .env
├── requirements.txt
├── Makefile
└── README.md
```

## Prerequisites

- Python 3.10+
- pip
- Virtual environment tool (`venv` recommended)
- Optional: Docker and Docker Compose

## Local Development Setup

### 1. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn app.main:app --reload
```

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Run Background Worker

```bash
celery -A workers.celery_worker worker --loglevel=info
```

## Run Tests

```bash
pytest -q
```

## Run with Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

## Environment Variables

Add values to `.env` (example):

```env
APP_ENV=development
APP_PORT=8000
DATABASE_URL=sqlite:///./genomic.db
REDIS_URL=redis://localhost:6379/0
```

## Current Status

This repository currently contains the project scaffold. Core pipeline logic and production-grade integrations should be implemented in the corresponding modules.
