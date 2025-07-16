#!/usr/bin/python3
"""
This module provides a function to serialize Python objects
to a JSON-formatted file.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be serialized (e.g., dict, list, str, int, etc.).
        filename (str): The name of the file to write the JSON string to.

    Note:
        If the object is not serializable (e.g., a set), a TypeError will be raised.
        Exceptions such as permission errors or serialization issues are not handled.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

