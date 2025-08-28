FROM python:3.11-slim

# Install curl to fetch uv installer
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (https://docs.astral.sh/uv/) and add to path
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Copy project metadata (dependencies) first to leverage Docker layer caching
COPY 

# Install dependencies into a project-local virtual environment (.venv)
# --frozen uses the lockfile if present;
RUN 

# Copy application code
COPY 

# Expose HTTP port
EXPOSE 

# Start the API using uv's runner
CMD [...]