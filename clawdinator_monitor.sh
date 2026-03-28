#!/bin/bash
MAX_THROUGHPUT=8000
CURRENT_LOAD=0
for i in {1..100}; do
    CURRENT_LOAD=$(( RANDOM % 10000 ))
    if [ $CURRENT_LOAD -gt $MAX_THROUGHPUT ]; then
        echo "Violation detected: $CURRENT_LOAD"
    fi
    sleep 1
done
