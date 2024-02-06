#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list is required\n");
        return;
    }
    setbuf(stdout, NULL);
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, typeName);
    }
    fflush(stdout);
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[*] Python bytes object is required\n");
        return;
    }
    setbuf(stdout, NULL);
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; ++i) {
        printf(" %02hhx", ((char *)PyBytes_AsString(p))[i]);
    }
    printf("\n");
    fflush(stdout);
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[*] Python float object is required\n");
        return;
    }
    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
    fflush(stdout);
}

