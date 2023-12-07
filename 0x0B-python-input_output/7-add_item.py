#!/usr/bin/python3
"""load, add, save"""


import sys
import json


with open('add_item.json', 'r', encoding='utf-8') as file:
    x = json.load(file)

x.extend(sys.argv[1:])

with open('add_item.json', 'w', encoding='utf-8') as file:
    json.dump(x, file)
