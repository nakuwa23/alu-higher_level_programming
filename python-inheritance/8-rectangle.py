#!/usr/bin/python3
"""This module shows inheritance"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle class"""

    def __init__(self, width, height):
        """This is the instantiator function"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
