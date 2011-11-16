#!/bin/bash

# Parse command line arguments.
if [ ${#@} -ne 2 ]; then
    echo "Usage: $0 <INPUT-DIR> <OUTPUT-DIR>"
    exit 1
fi
INP_DIR="$1"
OUT_DIR="$2"

# Create output directory, if necessary.
mkdir -p "$OUT_DIR"

# Copy every input file to the destination directory.
find "$INP_DIR" -type f | while read INP_FILE; do
    HASH=$(md5sum "$INP_FILE" | awk '{print $1}')
    OUT_FILE="$OUT_DIR/$HASH.txt"
    fold -s "$INP_FILE" >"$OUT_FILE"
done
