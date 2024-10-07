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

Docstrings are very useful for understanding what a piece of code is supposed to do, especially when you or someone else revisits the code later¹².

