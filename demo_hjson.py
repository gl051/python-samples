#!/usr/bin/env python

"""Demoing json."""

import hjson
from random import random

FILENAME = "./input/sample1.hjson"

dict_config = {}

# Read the file
with open(FILENAME, 'r') as f:
    content = f.read()
    dict_config = hjson.loads(content)

for key in dict_config.keys():
    print(dict_config[key]['func'])

print('test')
prop_name = 'age'
print(dict_config[prop_name])
if prop_name in dict_config.keys():
    if 'range' in dict_config[prop_name].keys():
        rtval = random.choice(dict_config[prop_name]['range'])
    elif 'func' in dict_config[prop_name].keys():
        rtval = dict_config[prop_name]['func']
print(rtval)
