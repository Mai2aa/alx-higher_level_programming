#!/usr/bin/python3
"""this is a script that adds all arguments to python list"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


items = load_from_json_file('add_item.json') or []
items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')
