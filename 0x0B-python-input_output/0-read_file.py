#!/usr/bin/python3
import sys
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())