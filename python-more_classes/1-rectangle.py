#!/usr/bin/python3
"""This is a rectangle class that does nothing"""


class Rectangle:
    """
    This is a rectangle class that stores
    a size and can calculate the area
    """

    def __init__(self, width=0, height=0):
        """This function initializes the class"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """This function returns the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """This function allows you to change the value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This function returns the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """This function allows you to change the value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
