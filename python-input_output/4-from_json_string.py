#!/usr/bin/python3
"""
This module returns a Python object from a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python object (e.g., dict, list).
    """
    return json.loads(my_str)
