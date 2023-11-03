#!/usr/bin/python
if __name__ == '__main__':
    import sys
    import math
    result = 0
    for i in sys.argv[1:]:
        result = result + int(i)
    print("{}".format(result))
