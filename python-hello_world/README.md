# python3 "$PYFILE"
Runs a Python script with the file name saved in the environment variable $PYFILE.

# python3 -c "$PYCODE"
Runs Python code stored in the $PYCODE environment variable.

# print("\"Programming is like building a multilingual puzzle")
Prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

# number = 98
print(f"{number:d} Battery street")
Prints the integer stored in the variable number, followed by Battery street, followed by a new line.

# number = 3.14159
print(f"Float: {number:.2f}")
Prints the float stored in the variable number with a precision of 2 digits.

# #!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])

Prints 3 times a string stored in the variable str, followed by its first 9 characters.

# #!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str3 = str1 + " " + str2
print(f"Welcome to {str3}!")

Prints Welcome to Holberton School!
