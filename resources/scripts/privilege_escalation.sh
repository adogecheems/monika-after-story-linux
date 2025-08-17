#!/bin/bash

ALLOWED_FUNCS=("read" "write" "access" "remove")

SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"

func_name="$1"
shift
if [[ ! " ${ALLOWED_FUNCS[@]} " =~ " ${func_name} " ]]; then
    echo "Unallowed function: $func_name"
    exit 1
fi

check_path() {
    local path="$1"
    local abs_path="$(realpath "$path")"
    if [[ "$abs_path" != "$SCRIPT_DIR"* ]]; then
        echo "Unallowed path: $path"
        exit 1
    fi
}

case "$func_name" in
    read)
        path="$1"
        check_path "$path"
        python2 -c "import sys; f=open('$path','r'); sys.stdout.write(f.read()); f.close()"
        ;;
    write)
        path="$1"
        content="$2"
        check_path "$path"
        python2 -c "f=open('$path','w'); f.write('$content'); f.close()"
        ;;
    access)
        path="$1"
        mode="$2"
        check_path "$path"
        python2 -c "import os, sys; sys.exit(0) if os.access('$path', int('$mode')) else sys.exit(1)"
        ;;
    remove)
        path="$1"
        check_path "$path"
        python2 -c "import os; os.remove('$path')"
        ;;
esac
