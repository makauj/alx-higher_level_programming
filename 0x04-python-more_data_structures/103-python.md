# CPython #1: PyBytesObject
## Task
Create two C functions that print some basic info about Python lists and Python bytes objects.

1. Python lists:
    - Prototype: `void print_python_list(PyObject *p);`

2. Python bytes:
    - Prototype: `void print_python_bytes(PyObject *p);`
    - Line “first X bytes”: print a maximum of 10 bytes
    - If p is not a valid PyBytesObject, print an error message (see example)
    - Read /usr/include/python3.4/bytesobject.h
About:
    - Python version: 3.4
    - Your shared library will be compiled with this command line: 
    ```bash
    gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
    ```

You are not allowed to use the following macros/functions:
    - `Py_SIZE`
    - `Py_TYPE`
    - `PyList_GetItem`
    - `PyBytes_AS_STRING`
    - `PyBytes_GET_SIZE`

## Overview of my solution
The code includes two functions that print details about Python list and bytes objects, respectively. It leverages the Python C API to interact with these objects directly.
#### Includes
- `Python.h`: This is the main header for the Python C API and includes everything needed to work with Python objects.
- `stdio.h`: Standard input/output header for using functions like printf.
- `object.h`, `listobject.h`, `bytesobject.h`: These headers define the internal structures of Python objects, including lists and bytes.

#### Function Prototypes
```c
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
```

### `print_python_list`
```c
void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size; // Get size from the PyVarObject structure
    list = (PyListObject *)p; // Cast to PyListObject

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated); // Print allocated size

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)p)->ob_item[i]; // Get each item
        printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name); // Print element type
        if (PyBytes_Check(obj)) // Check if the element is a bytes object
            print_python_bytes(obj); // Call the bytes function
    }
}
```
**Breakdown**
1. Parameters: `PyObject *p` is the Python object passed to the function.
2. Variables:
    - `size`: Holds the number of elements in the list.
    - `i`: Loop index.
    - `list`: A pointer to the list object.
    - `obj`: A pointer to each object in the list.
3. Getting Size:
    - `size = ((PyVarObject *)(p))->ob_size;`: Accesses the size of the list by casting the `PyObject` pointer to `PyVarObject`. This allows access to the `ob_size` attribute, which indicates the number of elements.
4. Casting to PyListObject:
    - `list = (PyListObject *)p;`: Casts the `PyObject` pointer to a `PyListObject`, which gives access to list-specific attributes.
5. Printing Info:
    - Prints the list information, including size and allocated space.
6. Iterating Over List Elements:
    - The loop iterates through each element of the list:
    - `obj = ((PyListObject *)p)->ob_item[i];`: Accesses each item in the list.
    - Prints the index and type name of each object using `((obj)->ob_type)->tp_name`.
    - If the object is a bytes object, it calls `print_python_bytes(obj)` to print its details.
7. Output: Prints basic information about the list, including its size and allocated memory.
### `print_python_bytes`
```c
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) // Check if the object is a bytes object
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size; // Get size
    string = ((PyBytesObject *)p)->ob_sval; // Get the string value

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size; // Determine limit for printing bytes

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        if (string[i] >= 0)
            printf(" %02x", string[i]); // Print byte in hex format
        else
            printf(" %02x", 256 + string[i]); // Handle negative bytes
    }

    printf("\n");
}
```
**Breakdown**
1. Parameters: Similar to the previous function.
2. Local Variables:
    - `string`: To hold the raw byte data.
    - `size`: To store the size of the bytes object.
    - `i`: Used for iteration.
    - `limit`: Determines how many bytes to print.
3. Validation:
    - `if (!PyBytes_Check(p))`: It checks if p is a valid bytes object using PyBytes_Check. If not, it prints an error message.
4. Size and Raw Data:
    - `size = ((PyVarObject *)(p))->ob_size;`: Gets the size of the bytes object.
    - `string = ((PyBytesObject *)p)->ob_sval;`: Retrieves the raw string of bytes.
5. Output Information:
    - Prints the size of the bytes and the string itself.
6. Limit for Printing: The limit is set to 10 or the size of the bytes, whichever is smaller.
7. Printing Bytes:
    - A loop iterates through the determined limit, printing each byte in hexadecimal format. It accounts for signed values to ensure they are displayed correctly.