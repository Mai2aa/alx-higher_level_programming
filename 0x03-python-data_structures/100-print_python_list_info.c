#include "Python.h"
/**
 * print_python_list_info - prints python list
 * @p: python object
*/
void print_python_list_info(PyObject *p)
{
	PyListObject *m;
	int i;
	int elements;

	m = (PyListObject *)p;
	elements = (int)m->ob_base.ob_size;

	printf("[*] Size of the Python List = %d\n", elements);
	printf("[*] Allocated = %ld\n", m->allocated);

	for (i = 0; i < elements; i++)
	{
		printf("Element %d: %s\n", i, m->ob_item[i]->ob_type->tp_name);
	}
}
