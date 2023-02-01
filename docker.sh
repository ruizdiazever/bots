#!/usr/bin/env bash

# Docker
docker image build -t ants .           # Build with detach mode in .
echo 'IMAGE OF DOCKER BUILDED'              # INFO
docker run -td ants                    # RUN in background
echo 'READY AND RUNNING IN BACKGROUND'