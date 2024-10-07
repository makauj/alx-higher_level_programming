# 0x08. Python - More Classes and Objects

Repo for learning more about OOP

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
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

## Tasks

#### 1. Basic Rectangle Class (0-rectangle.py)
- **Attributes**: 
  - Private instance attribute: `width`
  - Private instance attribute: `height`
- **Properties**: 
  - `width`: Getter and setter with type and value checks
  - `height`: Getter and setter with type and value checks
- **Initialization**: 
  - `__init__(self, width=0, height=0)`
- **Constraints**: 
  - Width and height must be integers and >= 0.

#### 2. Rectangle with Area and Perimeter (1-rectangle.py)
- Adds public instance methods:
  - `area(self)`: Returns the area of the rectangle.
  - `perimeter(self)`: Returns the perimeter, which is 0 if width or height is 0.

#### 3. Enhanced Rectangle with String Representation (2-rectangle.py)
- Adds:
  - `__str__()`: Prints the rectangle with `#` character.
  - Returns an empty string if width or height is 0.

#### 4. Rectangle with `repr()` Method (3-rectangle.py)
- Adds:
  - `__repr__()`: Provides a string representation for instance recreation with `eval()`.

#### 5. Rectangle with Deletion Message (4-rectangle.py)
- Adds:
  - A message printed when an instance is deleted.

#### 6. Rectangle Instance Counter (5-rectangle.py)
- Adds a class attribute:
  - `number_of_instances`: Tracks the number of instances created and deleted.

#### 7. Custom Print Symbol (6-rectangle.py)
- Adds:
  - `print_symbol`: Class attribute used for string representation.

#### 8. Bigger or Equal Method (7-rectangle.py)
- Adds a static method:
  - `bigger_or_equal(rect_1, rect_2)`: Returns the rectangle with the larger area.

#### 9. Class Method for Square (8-rectangle.py)
- Adds:
  - `square(cls, size=0)`: Returns a new rectangle instance where width and height are equal to size.

## N Queens Problem Solver
### Description
- Solves the N Queens puzzle by placing N non-attacking queens on an N×N chessboard.
  
### Usage
- **Command**: `nqueens N`
- **Validation**:
  - If the wrong number of arguments is provided, prints `Usage: nqueens N` and exits with status 1.
  - If `N` is not an integer, prints `N must be a number` and exits with status 1.
  - If `N` is less than 4, prints `N must be at least 4` and exits with status 1.

### Output
- Prints every possible solution to the N Queens problem, one solution per line.

### Constraints
- You are only allowed to import the `sys` module.