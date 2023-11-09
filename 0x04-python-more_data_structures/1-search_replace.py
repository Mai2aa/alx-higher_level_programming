#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = []
    for i in my_list:
        if i == search:
            new = my_list.index(i)
            replace = new
            lst.append(replace)
        else:
            lst.append(i)
    return lst