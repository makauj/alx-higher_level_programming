#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    const char *val;
    const char *type;

	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = PyUnicode_GetLength(p);
	val = PyUnicode_AsUTF8(p);
	type = PyUnicode_KIND(p) == 1 ? "compact ascii" : "compact unicode object";

	printf("[.] string object info\n");
	printf("  type: %s\n", type);
	printf("  length: %zd\n", len);
	printf("  value: %s\n", val);
}
