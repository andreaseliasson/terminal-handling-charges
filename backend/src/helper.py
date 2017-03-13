import json


def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def dump_json(charges, file_name):
    with open(file_name, 'w') as fp:
        json.dump(charges, fp)
