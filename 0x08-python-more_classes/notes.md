# Python OOP Classes and Methods
In Python, we use blocks of statements to manipultate data in what is refered to as procedure-oriented programming. Another way of organizing a program is combining data and functionality by wrapping it inside an object.

Precedural programming is fine for most small tasks but for large programs, Object Oriented Progamming(OOP) is better.

The main aspects of OOP are `classes` and `objects`.

A **class** creates a new `type` where **objects** are instances of the class.
**Objects** can store data, belonging to the object, using ordinary variables. They can also have functionality byt using functions that belong to a class. These functions are called methods of the calss.

This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

## __doc__
In Python, `__doc__` is a special attribute that stores the documentation string (docstring) for a module, class, method, or function. Docstrings are used to describe what the object does and are typically enclosed in triple quotes (`'''` or `"""`). They provide a convenient way to access descriptive texts about the code's functionality.

Here's an example:

```python
class Dog:
    """Your best friend."""

    def bark(self):
        """Make the dog bark."""
        return "Woof!"

print(Dog.__doc__)  # Output: Your best friend.
print(Dog.bark.__doc__)  # Output: Make the dog bark.
```

In this example:
- `Dog.__doc__` returns the docstring of the `Dog` class.
- `Dog.bark.__doc__` returns the docstring of the `bark` method.

Docstrings are very useful for understanding what a piece of code is supposed to do, especially when you or someone else revisits the code later.

## __del__
This method is know as a destructor. It is called when the reference countdrops to zero or when the Python interpreter shuts down. As you can note, this is when an object is about to be destroyed.
**`__del__`** allows you to define the specific cleanup actions that should be taken during garbage collection. This includes releasing external resources like file handles, network connections or database connections

#### Example
```python
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.file.write("Some initial data")
        print("File opened and written to")

    def __del__(self):
        print("Closing file")
        self.file.close()

# Creating a FileHandler object
file_handler = FileHandler('example.txt')

# Deleting the object explicitly (calls __del__ method)
del file_handler
```
**output**
```
File opened and written to
Closing file
```
#### Key Points
1. **Automatic Call:** `__del__` is automatically called by the arbage collector when an object's reference count drops to zero.
2. **Resource Cleanup:** usefulf for cleaning up resources eg. files, network or database connections etc.
3. **Silent Exceptions:** If an exception occurs inside  the `__del__` method, no exceptions are raised.

However, it’s generally recommended to use context managers (with the `with` statement) for resource management, as they provide a more reliable and explicit way to handle resource cleanup.

## __str__
The `__str__` method in Python is a special method used to define the "informal" or nicely printable string representation of an object. This method is called by the `str()` built-in function and by the `print` function to convert the object into a string¹².

#### Example
Here's an example to illustrate how `__str__` works:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

car = Car("Toyota", "Corolla", 2020)
print(car)  # Output: 2020 Toyota Corolla
```

#### Key Points
1. **Customization**: The `__str__` method allows you to customize how an object is represented as a string.
2. **Readability**: It should return a string that is easy to read and provides a useful description of the object.
3. **Usage**: This method is automatically called when you use `print()` or `str()` on an instance of the class.

### Sources
¹: [Python Tutorial](https://www.pythontutorial.net/python-oop/python-__str__/)
²: [Real Python](https://realpython.com/lessons/how-and-when-use-str/)

## __repr__
This is a special method in Python used to define the "official" string representation of an object. It is called by the `repr()` built-in function and is intended to provide a string that could, ideally, be used to redreate the object.
**__repr__** is useful for debugging and logging as it give a clear and unambiguous representation of the object.

#### Example

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}", "{self.last_name}", {self.age})'

person = Person("John", "Doe", 30)
print(repr(person))  # Output: Person("John", "Doe", 30)
```

#### Key points
1. **Reproducibility:** The string returned by `__repr__` should, if possible, be a valid Python expression that can be used to recreate the object.
2. **Debugging:** It provides a detailed and unambiguous representation of the object, which is useful for debugging
3. **Fallback for `__str__`:**  If a class does not implement `__str__`, the `__repr__` method is used as a fallback when `str()` is called on an instance of the class.

#### Difference Between `__repr__` and `__str__`
| `__repr__` | `__str__` |
|------------|-----------|
| Aimed at developers, providing a detailed and unambiguous representation of the object. | Aimed at end-users, providing a readable and informal string representation of the object. |
