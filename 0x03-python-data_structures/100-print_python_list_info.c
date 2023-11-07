#include "Python.h"
void print_python_list_info(PyObject *p)
{
    pyListObject *m;
    int i; 
    int elements;
    m = (pyListObject *)p;

    elements = (int)m->ob_base.ob_size;
    printf("[*] Size of the Python List = %d\n", elements);
    printf("[*] Allocated = %d\n", m->allocated);

    for (i = 0; i < elements; i++)
    {
        printf("Element %d: %s\n", i, m->ob_item[i]->ob->type->tp_name);
    }
    
}