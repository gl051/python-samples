""" Demo loading and saving JSON"""
import json
from pprint import pprint


def deserialize(filename):
    with open(filename, 'r') as f:
        # you can build the json directly from the file reader
        json_data = json.load(f)
        # Depending on the JSON format you get a different JSON object
        if isinstance(json_data, dict):
            print('json passed is an array --> python object is a dict')
            print('keys() = {}'.format(json_data.keys()))
        elif isinstance(json_data, list):
            print('json passed is an array --> python object is a list')
            print('len() = {}'.format(len(json_data)))
        else:
            print(type(json_data))
        return json_data


def serialize(filename, object_to_serialize):
    with open(filename, 'w+') as fout:
        json.dump(object_to_serialize, fout, indent=4)
        pprint(object_to_serialize)
        print('Saved to {}'.format(filename))

# Running the demo


print(">>> Serialize JSON")
deserialize('./samples/json/in1.json')

print(">>> Deserialize JSON")
sample = {'name': 'Mark', 'age': 34, 'scores': [34.5, 45.1, 90.3]}
serialize('./samples/json/out1.json', sample)

sample = [{'code': 'A'}, {'code': 'B'}]
serialize('./samples/json/out2.json', sample)
