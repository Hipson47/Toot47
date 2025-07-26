# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy dependency files and install
# This will also generate a poetry.lock file if it doesn't exist
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy the application source code
COPY src/ ./src/

# Copy .env file for configuration
COPY .env* ./ 

EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "src.toot47.api.main:app", "--host", "0.0.0.0", "--port", "8000"] 