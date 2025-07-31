#!/bin/bash
# Script to retrieve supported HTTP methods from the URL using curl
curl -sI -X OPTIONS "$1" | grep -i '^Allow:' | cut -d' ' -f2-
