# CPython

## Introduction
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

## Question
Create a C function that prints some basic info about Python lists.

	- Prototype: void print_python_list_info(PyObject *p);
	- Format: see example
	- Python version: 3.4
	- Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
	- OS: Ubuntu 14.04 LTS

### How I understood the problem
Implement a C function that prints detailed information about Python lists.
This information should include:
	- The size of the list.
	- Allocated space.
	- Type of each element

### Steps to Solve
1. Include necessary Headers
```
#include <Python.h>
#include <object.h>
#include <listobject.h>
```

2. Function Definition
```
void print_python_list_info(PyObject *p)
```

3. Extract List Information
	- Use `PyList_Size` to get the number of elements in the list
	- Access internal details of the `PListObject` to find the allocated size. This directly uses Python's internal structure

4. Print Information
	- Print the size of the list
	- Print the allocated space for the list
	- Loop through each element in the list and print its type

## Pseudocode
```
#include <Python.h>
#include <stdio.h>

/**
 * Function to print Python list info
 */
void print_python_list_info(PyObject *p)
{
	/* Step 2: Get the size of the list */
	Py_ssize_t size = PyList_Size(p);
	
	printf("[*] Size of the Python List = %zd\n", size);

	/* Step 3: Get the allocated size */
	/* Access internal PyListObject structure */
	PyObject **items = ((PyListObject *)p)->ob_item;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %zd\n", allocated);

	/* Step 4: Print types of each element in the list */
	for (Py_ssize_t i = 0; i < size; i++) 
	{
		PyObject *item = PyList_GetItem(p, i);
		/* Print the type of each item */
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
```
