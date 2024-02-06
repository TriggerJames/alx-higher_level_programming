#include "py_obj_info.h"
/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: A pointer to a Python object.
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
/**
 * print_python_bytes - Prints some basic info about Python bytes.
 * @p: A pointer to a Python object.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	size = Py_SIZE(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i < size && i < 10; i++)
		printf(" %02hhx", str[i]);

	if (size >= 10)
		printf(" %02hhx", str[10]);

	printf("\n");
}
/**
 * print_python_float - Prints some basic info about Python float objects.
 * @p: A pointer to a Python object.
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %g\n", value);
}
