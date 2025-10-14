#!/bin/bash

# show system environment and create project environment

echo "=======System Environment==========="
echo "User: $USER"
echo "Home: $HOME"
echo "Shell: $SHELL"
echo ""

# Count Path Directories
IFS=: read -ra paths <<<"$PATH"
echo "Path has ${#paths[@]} directories "

# create project Environment with Defaults

export PROJECT_NAME="${PROJECT_NAME:-MyApp}"
export PROJECT_ENV="${PROJECT_ENV:-PROD}"
export PROJECT_PORT="${PROJECT_PORT:-8080}"

echo ""

echo "===Project Environemnt===="
echo "NAME: $PROJECT_NAME"
echo "ENVIRONMENT: $PROJECT_ENV"
echo "PROD: $PROJECT_PORT"



