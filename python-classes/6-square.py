#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores properties of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiator function"""

        self._size = size

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = position

    def area(self):
        """This function returns the area of the square"""

        return self._size**2

    def my_print(self):
        """This function print a square using # as blocks in a 2D plane"""

        if self._size == 0:
            print("")
            return 0

        print('\n'*self._position[1], end='')
        for i in range(self._size):
            print(' '*self._position[0], end='')
            print('#'*self._size)

    @property
    def size(self):
        """This function returns the value of size"""

        return self._size

    @size.setter
    def size(self, value):
        """This function allows you to change the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def position(self):
        """This function returns the value of position"""

        return self._position

    @position.setter
    def position(self, value):
        """This function allows you to change the value of position"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value
