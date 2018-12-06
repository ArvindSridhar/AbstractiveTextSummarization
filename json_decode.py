#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supports conversion between json and list of list of list of strings
"""
import json

## Given the full filename, de-serialize and convert json object to documents 
## in the form of a dictionary
## key: document index
## value: document represented as a list of list of strings
def load_json_to_dict(filename):
    with open(filename, 'r') as infile:
        dictionary = json.load(infile)
    return dictionary

## Serialize the dictionary and write to a json file with the given filename ("__.json")
def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile)
    return
