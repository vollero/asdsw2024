#!/usr/bin/bash

# Check if a pattern was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <pattern>"
    exit 1
fi

pattern=$1

# Kill processes matching the pattern
pkill -f $pattern

# Check if pkill succeeded
if [ $? -eq 0 ]; then
    echo "All processes matching '$pattern' have been killed."
else
    echo "Failed to kill some or all processes matching '$pattern'."
fi

