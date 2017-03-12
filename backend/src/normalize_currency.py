import requests
import json
from helper import load_json
import copy


def get_unique_currencies(charges_list):
    unique_currencies = set([charge['currency'] for charge in charges_list])
    return unique_currencies


def get_currency_exchange_rates_from_api(currencies, base_currency='USD'):
    params = {
        'app_id': '2190c26ff7a84a31ade9f7f57ddb33a8',
        'base': base_currency,
    }
    r = requests.get('https://openexchangerates.org/api/latest.json', params)
    resp = r.json()
    all_currency_rates = resp['rates']

    currencies_exl_usd = [currency for currency in currencies if currency != 'USD']
    relevant_currency_rates = {}
    for currency in currencies_exl_usd:
        relevant_currency_rates[currency] = all_currency_rates[currency]

    # Dump relevant currency rates to .json file to limit API calls
    with open('../data/currency_rates.json', 'w') as fp:
        json.dump(relevant_currency_rates, fp, indent=2)

    return relevant_currency_rates


def get_currency_exchange_rates_from_file(file_name):
    currency_rates = load_json(file_name)
    return currency_rates


def normalize_charges(charges, currency_rates):
    normalized_charges = []
    for charge in charges:
        if charge['currency'] != 'USD':
            normalized_charge = copy.deepcopy(charge)
            normalized_charge['value'] = charge['value'] / currency_rates[charge['currency']]
            normalized_charges.append(normalized_charge)
        else:
            normalized_charges.append(charge)
    print('normalized charges')
    print(normalized_charges[:3])
    return normalized_charges
