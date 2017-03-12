import json


def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def get_2_letter_country_codes(charges):
    unique_country_codes = set([charge['port'][:2] for charge in charges])
    return unique_country_codes
