# 0x13. JavaScript - Objects, Scopes and Closures

## Learning Objectives

- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Tasks

0. Write an empty class Rectangle that defines a rectangle:
    - You must use the `class` notation for defining your class.

1. Write a class Rectangle that defines a rectangle:

    - You must use the `class` notation for defining your class
    - The constructor must take 2 arguments `w` and `h`
    - Initialize the instance attribute `width` with the value of `w`
    - Initialize the instance attribute `height` with the value of `h`

2. Write a class Rectangle that defines a rectangle:

    - You must use the `class` notation for defining your class
    - The constructor must take 2 arguments `w` and `h`
    - Initialize the instance attribute `width` with the value of `w`
    - Initialize the instance attribute `height` with the value of `h`
    - If `w` or `h` is equal to 0 or not a positive integer, create an empty object

3. Write a class Rectangle that defines a rectangle:

    - You must use the `class` notation for defining your class
    - The constructor must take 2 arguments `w` and `h`
    - Initialize the instance attribute `width` with the value of `w`
    - Initialize the instance attribute `height` with the value of `h`
    - If `w` or `h` is equal to 0 or not a positive integer, create an empty object
    - Create an instance method called `print()` that prints the rectangle using the character `X

4. Write a class Rectangle that defines a rectangle:

    - You must use the `class` notation for defining your class
    - The constructor must take 2 arguments `w` and `h`
    - Initialize the instance attribute `width` with the value of `w`
    - Initialize the instance attribute `height` with the value of `h`
    - If `w` or `h` is equal to 0 or not a positive integer, create an empty object
    - Create an instance method called `print()` that prints the rectangle using the character `X`
    - Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
    - Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

5. Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

    - You must use the `class` notation for defining your class and `extends`
    - The constructor must take 1 argument: `size`
    - The constructor of `Rectangle` must be called (by using `super()`)

6. Write a class Square that defines a square and inherits from Square of 5-square.js:

    - You must use the `class` notation for defining your class and `extends`
    - Create an instance method called `charPrint(c)` that prints the rectangle using the - character `c`
    - If `c` is `undefined`, use the character `X`

7. Write a function that returns the number of occurrences in a list:

    - Prototype: `exports.nbOccurences = function (list, searchElement)`

8. Write a function that returns the reversed version of a list:

    - Prototype: exports.esrever = `function (list)`
    - You are not allow to use the built-in method `reverse`

9. Write a function that prints the number of arguments already printed and the new argument value. (see example below)

    - Prototype: `exports.logMe = function (item)`
    - Output format: `<number arguments already printed>: <current argument value>`

    **Example**

    ```bash
    guillaume@ubuntu:~/0x13$ cat 9-main.js
    #!/usr/bin/node
    const logMe = require('./9-logme').logMe;

    logMe("Hello");
    logMe("Best");
    logMe("School");

    guillaume@ubuntu:~/0x13$ ./9-main.js
    0: Hello
    1: Best
    2: School
    guillaume@ubuntu:~/0x13$ 
    ```

10. Write a function that converts a number from base 10 to another base passed as argument:

    - Prototype: exports.converter = function (base)
    - You are not allowed to import any file
    - You are not allowed to declare any new variable (var, let, etc..)

11. Write a script that imports an array and computes a new array.

    - Your script must import `list` from the file `100-data.js`
    - You must use a `map`. [Tips](https://intranet.alxswe.com/rltoken/LOEW51ZbYDjO4KZCFevzNQ)
    - A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
    - Print both the initial list and the new list

12. Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

    - Your script must import `dict` from the file `101-data.js`
    - In the new dictionary:
        - A key is a number of occurrences
        - A value is the list of user ids
    - Print the new dictionary at the end

13. Write a script that concats 2 files.

    - The first argument is the file path of the first source file
    - The second argument is the file path of the second source file
    - The third argument is the file path of the destination
