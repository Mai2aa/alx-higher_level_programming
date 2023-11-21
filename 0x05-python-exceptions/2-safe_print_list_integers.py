#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                count += 1
                if count == x:
                    break
        print()
    except (TypeError):
        return
    return count