#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores properties of a square"""

    def __init__(self, size=0):
        """Initiator function"""

        self._Square__size = size

    def area(self):
        """This function returns the area of the square"""

        return self._Square__size**2

    @property
    def size(self):
        """This function returns the value of size"""

        return self._Square__size

    @size.setter
    def size(self, value):
        """This function allows you to change the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value
