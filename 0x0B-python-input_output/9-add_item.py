#!/usr/bin/python3
"""This module adds all arguments to a Python list,
and then save them to a file"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []
args = len(sys.argv)
if args < 2:
    save_to_json_file(my_list, "add_item.json")
else:
    for i in range(1, args):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
