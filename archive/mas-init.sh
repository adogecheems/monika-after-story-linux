#!/bin/bash

# Create temporary directory and restrict permissions
TMP_DIR=$(mktemp -d "/tmp/masenv.${USER}.XXXXXXXXXXXX") || exit 1
chmod 700 "$TMP_DIR"

# Get home directory and runtime directory
HOME=$(getent passwd "$USER" | cut -d: -f6)
XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR:-"/run/user/$(id -u)"}

# Generate environment variables
PULSE_SERVER=${PULSE_SERVER:-"unix:$XDG_RUNTIME_DIR/pulse/native"}
PULSE_COOKIE="$TMP_DIR/pulse_cookie"

# Copy current user's pulse cookie
for src in "$XDG_RUNTIME_DIR/pulse/cookie" "$HOME/.config/pulse/cookie"; do
    if [[ -f "$src" && -r "$src" ]]; then
        cp -f "$src" "$PULSE_COOKIE"
        break
    fi
done

# Check if cookie file exists
if [[ ! -f "$PULSE_COOKIE" ]]; then
    echo "Error: Valid PulseAudio cookie file not found" >&2
    rm -rf "$TMP_DIR"
    exit 1
fi

# Save environment variables to config file
ENV_FILE="$TMP_DIR/envs"
cat > "$ENV_FILE" <<EOF
export PULSE_SERVER="$PULSE_SERVER"
export PULSE_COOKIE="$PULSE_COOKIE"
export HOME="$HOME"
EOF

# Transfer control via pkexec
pkexec /opt/MAS/mas-launch.sh "$TMP_DIR"

# Clean up temporary files
rm -rf "$TMP_DIR"