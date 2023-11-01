#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch = ""
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            ch = ch + chr(ord(i) - 32)
            print("{:s}".format(ch), end="")
        else:
            ch = ch + i
            print("{:s}".format(ch), end="")
    print()
