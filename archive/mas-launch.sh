#!/bin/bash

# Validate argument
if [[ $# -ne 1 || ! -d "$1" ]]; then
    echo "Error: Invalid temporary directory argument" >&2
    exit 1
fi

TMP_DIR="$1"
ENV_FILE="${TMP_DIR}/envs"

# Check if environment file exists
if [[ ! -f "$ENV_FILE" ]]; then
    echo "Error: Environment configuration file not found" >&2
    exit 1
fi

# Load environment variables
. "$ENV_FILE"

# Validate variables
if [[ -z "$PULSE_SERVER" || ! -f "$PULSE_COOKIE" ]]; then
    echo "Error: Invalid audio environment configuration" >&2
    exit 1
    elif [ "$HOME" == "/root" ]; then
    echo "Error: Failed to switch to user directory" >&2
    exit 1
fi

if [[ ! -x "/opt/MAS/DDLC.sh" ]]; then
    echo "Error: MAS does not exist or is not executable" >&2
    exit 1
fi

# Launch target program
exec /opt/MAS/DDLC.sh