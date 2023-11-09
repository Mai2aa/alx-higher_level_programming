#!/usr/bin/python3
from pdb import lasti2lineno


def search_replace(my_list, search, replace):
    lst = []
    for i in my_list:
        if i == search:
            lst.append(replace)
        else:
            lst.append(i)
    return lst
