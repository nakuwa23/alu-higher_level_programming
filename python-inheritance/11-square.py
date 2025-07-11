#!/usr/bin/python3
"""This modules uses inheritance"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Just to pass the test"""
    def __init__(self, size):
        """Too tired to add documentation"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Maybe next time I'll add explanation"""

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
