# Install uv
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# Copy the project into the intermediate image
ADD . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable

ENV PATH="/app/.venv/bin:$PATH"

FROM python:3.12-slim

# Copy the environment, but not the source code
COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Run the application via the venv console script installed by pyproject [project.scripts]
CMD ["/app/.venv/bin/serve", "--host", "0.0.0.0", "--port", "8000"]

# OR ALTERNATIVELY

# CMD ["/app/.venv/bin/python", "-m", "uvicorn", "example_fastapi.app:app", "--host", "0.0.0.0", "--port", "8000"]

# OR using uvicorn directly

# CMD ["/app/.venv/bin/uvicorn", "example_fastapi.app:app", "--host", "0.0.0.0", "--port", "8000"]