#!/usr/bin/python3
"""This is a rectangle class that does nothing"""


class Rectangle:
    """
    This is a rectangle class that stores
    a size and can calculate the area
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """This function initializes the class"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height + self.__width) * 2

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result

        for i in range(self.__height):
            for j in range(self.__width):
                result += "{}".format(self.print_symbol)
            result += "\n" if i != (self.__height-1) else ""
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle by area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square"""
        return cls(size, size)
