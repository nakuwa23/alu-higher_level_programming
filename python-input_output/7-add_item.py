#!/usr/bin/python3
"""This script adds command-line arguments to a Python list
and saves them in a JSON file named add_item.json.

It uses the save_to_json_file and load_from_json_file functions
defined in 5-save_to_json_file.py and 6-load_from_json_file.py respectively.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else initialize as empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new command-line arguments
items.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(items, filename)
