#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores properties of a square"""

    def __init__(self, size=0):
        """Initiator function"""

        self._size = size

    def area(self):
        """This function returns the area of the square"""

        return self._size**2

    def my_print(self):
        """This function print a square using # as blocks"""

        if self._size == 0:
            print("")
            return 0

        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print("")

    @property
    def size(self):
        """This function returns the value of size"""

        return self._size

    @size.setter
    def size(self, value):
        """This function allows you to change the value of size"""

        try:
            if isinstance(value, int) and value > 0:
                self._size = value
            elif value < 0:
                raise ValueError
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
