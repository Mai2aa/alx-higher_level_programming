#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            result[count] = True
        else:
            result[count] = False
    return result
