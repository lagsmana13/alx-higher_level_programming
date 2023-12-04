#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - shows info about Python lists
 * @p: object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p) {
    Py_ssize_t list_size, a, i;

    i = 0;
    PyObject *obj;

    list_size = PyList_Size(p);
    a = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", a);

    for (i = 0; i < list_size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
