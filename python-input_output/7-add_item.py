#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file as a JSON array.

Uses save_to_json_file from 5-save_to_json_file.py
and load_from_json_file from 6-load_from_json_file.py.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if the file exists; otherwise, use empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(items, filename)
