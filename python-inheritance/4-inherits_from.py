#!/usr/bin/python3
"""IDK I just want to pass the test"""


def inherits_from(obj, a_class):
    """This function check if obj is an instance of a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
