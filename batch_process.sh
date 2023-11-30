#!/bin/bash
# Make sure to give execute permissions with: chmod +x batch_process.sh
# Usage: ./batch_process.sh video_file lang1 lang2 lang3 ...

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 video_file lang1 [lang2 ...]"
    exit 1
fi

VIDEO_FILE="$1"
shift
LANGUAGES=("$@")

for LANG in "${LANGUAGES[@]}"; do
    echo "Processing $VIDEO_FILE into $LANG"
    python video_processor.py "$VIDEO_FILE" "$LANG" || { echo "Failed to process $VIDEO_FILE into $LANG"; exit 1; }
done
