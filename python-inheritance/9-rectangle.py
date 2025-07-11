#!/usr/bin/python3
"""This module shows inheritance"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle class"""

    def __init__(self, width, height):
        """This is the instantiator function"""
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """This function returns the area of a rectangle"""

        return self.__width * self.__height
