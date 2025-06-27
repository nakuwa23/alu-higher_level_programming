#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(f"{number} is ", end="")

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")

Prints whether the number stored in the variable number is positive or negative.
