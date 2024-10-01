# 0x06. Python - Classes and Objects

## Background Context

Object-oriented programming (OOP) is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects. Python is a multi-paradigm language; it supports imperative, functional, and procedural paradigms but its object-oriented programming is perhaps one of the most significant.
The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

## Learning Objectives

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## Tasks
0. Write an empty class `Square` that defines a square:
1. Write a class `Square` that defines a square by: (based on 0-square.py)
    - Private instance attribute: `size`
    - Instantiation with `size` (no type/value verification)
2. Write a class Square that defines a square by: (based on 1-square.py)
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0):
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
3. Write a class `Square` that defines a square by: (based on 2-square.py)
    - Private instance attribute: `size`
    - Instantiation with optional `size`: `def __init__(self, size=0):`
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        -   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    - Public instance method: `def area(self):` that returns the current square area
4. Write a class `Square` that defines a square by: (based on 3-square.py)
    - Private instance attribute: `size`:
        - property `def size(self):` to retrieve it
        - property setter `def size(self, value):` to set it:
            - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
            - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    - Instantiation with optional `size`: `def __init__(self, size=0):`
    - Public instance method: `def area(self):` that returns the current square area
5. Write a class `Square` that defines a square by: (based on 4-square.py)
    - Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
        - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    - Instantiation with optional `size: def __init__(self, size=0):`
    - Public instance method: `def area(self):` that returns the current square area
    - Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to `0`, print an empty line
6. Write a class `Square` that defines a square by: (based on 5-square.py)
    - Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    - Private instance attribute: `position`:
        - property `def position(self):` to retrieve it
        - property setter `def position(self, value):` to set it:
            - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
    - Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
    - Public instance method: `def area(self):` that returns the current square area
    - Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`:
        - if `size` is equal to `0`, print an empty line
        - `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
