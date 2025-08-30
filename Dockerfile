FROM 

# Install curl to fetch uv installer
RUN 

# Install uv (https://docs.astral.sh/uv/) and add to path
RUN

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