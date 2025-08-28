FROM python:3.11-slim

# Install curl to fetch uv installer
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (https://docs.astral.sh/uv/)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Copy project metadata first to leverage Docker layer caching
COPY pyproject.toml uv.lock* ./

# Install dependencies into a project-local virtual environment (.venv)
# --frozen uses the lockfile if present; --no-dev keeps image lean
RUN uv sync --frozen

# Copy application code
COPY ./app ./app

EXPOSE 8000

# Start the API using uv's runner
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]