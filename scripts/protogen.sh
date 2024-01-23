#!/bin/bash
set -e

# Get your host's UID and GID
export HOST_UID=$(id -u)
export HOST_GID=$(id -g)

# Build the Docker image
# podman build . -f Dockerfile -t your-image-name --build-arg UID=$HOST_UID --build-arg GID=$HOST_GID
podman-compose up --build
podman cp python_grpc_test_runner-task_1:/home/nonroot/app/gen/ ./protobuf/
