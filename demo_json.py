""" Demo loading and saving JSON"""
import json
from pprint import pprint

FOUT = "./input/sample1.json"

# --------------------------
# 1. Reading a JSON file
# --------------------------
with open(FOUT, 'r') as f:
    # you can build the json directly from the file reader
    json_data = json.load(f)

# Depending on the JSON format you get a different JSON object
if isinstance(json_data, dict):
    print ('json passed is an array --> python object is a dict')
    print ('keys() = {}'.format(json_data.keys()))
elif isinstance(json_data, list):
    print ('json passed is an array --> python object is a list')
    print ('len() = {}'.format(len(json_data)))
else:
    print (type(json_data))


# --------------------------
# 1. Writing a JSON file
# --------------------------
fake_data = [ {'name': 'Mark', 'score': 34.5},
                {'name': 'Julia', 'score': 40.6},
                {'name': 'Robert', 'score': 29.1}]

FOUT = './output/test.json'

with open(FOUT, 'w') as fout:
    json.dump(fake_data, fout)
pprint(fake_data)
print ('Save to {}'.format(FOUT))
