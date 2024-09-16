#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: A pointer to a Python object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	int i;
	const char *type_name;
	Py_ssize_t allocated;
	PyListObject *obj = (PyListObject *)p;

	allocated = obj->allocated;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocated);

	for (i = 0; i < size; i++)
	{
		type_name = Py_TYPE(obj->ob_item[i])->tp_name;
		printf("Element %i: %s\n", i, type_name);
	}
}
