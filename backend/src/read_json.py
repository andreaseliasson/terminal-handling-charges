import json


def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data
