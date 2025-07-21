# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.12.9
FROM python:${PYTHON_VERSION}-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.7.17 /uv /uvx /bin/

# # Enable bytecode compilation
# ENV UV_COMPILE_BYTECODE=1

# # Copy from the cache instead of linking since it's a mounted volume
# ENV UV_LINK_MODE=copy

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # Download dependencies as a separate step to take advantage of Docker's caching.
# # Leverage a cache mount to /root/.cache/uv to speed up subsequent builds.
# # Leverage a bind mount to uv.lock to avoid having to copy them into
# # into this layer.
# RUN --mount=type=cache,target=/root/.cache/uv \
#     --mount=type=bind,source=uv.lock,target=uv.lock \
#     --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#     uv sync --locked --no-install-project --no-dev


# Copy the source code into the container.
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Switch to the non-privileged user to run the application.
#USER appuser

# Place executables in the environment at the front of the path
#ENV PATH="/app/.venv/bin:$PATH"

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["uv", "run", "main.py"]
