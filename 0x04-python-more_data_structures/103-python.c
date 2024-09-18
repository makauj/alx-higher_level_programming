#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - print information about a Python list object
 * @p: object
 */
void print_python_list(PyObject *p)
{
	long size, i;
	if (!PyList_Check(p))
	{
		printf("Error: Invalid List Object\n");
		return;
	}

	size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %ld\n", size);

	/* Iterate through the list elements */
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - function prints info about a Python bytes object
 * @p: pointer to a python object
 */
void print_python_bytes(PyObject *p)
{
	long size, display_size, i;
	if (!PyBytes_Check(p))
	{
		printf("Error: Invalid Bytes Object\n");
		return;
	}
	
	size = PyBytes_Size(p);

	display_size = size < 10 ? size : 10;

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes: %ld\n", size);

	printf("[*] First %ld bytes: ", display_size);
	for (i = 0; i < display_size; i++)
	{
		printf("%02x ", (unsigned char) PyBytes_AsString(p)[i]);
	}
	printf("\n");
}