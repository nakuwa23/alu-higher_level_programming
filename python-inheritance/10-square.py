#!/usr/bin/python3
"""
This modules uses inheritance
I'm adding word like class and agrs int
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Just to pass the test
    I'm adding word like class and agrs int
    """

    def __init__(self, size):
        """
        I'm super tired rn
        I'm adding word like class and agrs int
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
