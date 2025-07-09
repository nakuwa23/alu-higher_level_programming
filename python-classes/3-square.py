#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores a size and can calculate the area"""

    def __init__(self, size=0):
        """This function checks if the argument is an integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """This function returns the area of the square"""

        return self._Square__size**2
