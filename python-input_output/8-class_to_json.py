#!/usr/bin/python3
"""
This module returns the dictionary description
with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    final_json = {}

    for name, value in obj.__dict__.items():
        final_json[name] = value

    return final_json
