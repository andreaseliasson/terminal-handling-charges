from flask import Flask
from flask import jsonify
from flask import request
import json
from helper import (load_json,
                    get_2_letter_country_codes,
                    get_country_charges_with_outliers,
                    is_outlier,
                    create_acc_charges,
                    save_new_charge)
from normalize_currency import (get_unique_currencies,
                                get_currency_exchange_rates_from_api,
                                get_currency_exchange_rates_from_file,
                                normalize_charges)
from outlier_detection import compare_outlier_methods

app = Flask(__name__)


@app.route("/")
def start():
    # charges = load_json('../data/sample_data.json')
    # currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    # normalized_charges = normalize_charges(charges, currency_rates)
    # country_charges = get_country_charges_with_outliers(normalized_charges, get_2_letter_country_codes(charges))
    #
    # return jsonify(country_charges)
    return ''


@app.route('/charge', methods=['POST'])
def submit_new_charge():
    new_charge = request.json

    return "posting"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return response

if __name__ == "__main__":
    # app.run()
    charges = load_json('../data/sample_data.json')
    # unique_currencies = get_unique_currencies(charges)
    # # rates = get_currency_exchange_rates_from_api(unique_currencies)
    currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    normalized_charges = normalize_charges(charges, currency_rates)
    country_charges = get_country_charges_with_outliers(normalized_charges, get_2_letter_country_codes(charges))
    #
    # # Distribution and outliers
    # # compare_outlier_methods(normalized_charges, get_2_letter_country_codes(charges))
    new_charge = {'currency': '1', 'value': '120', 'port': 'CNSHA', 'supplier_id': '2'}
    outlier = is_outlier(normalized_charges, new_charge)
    print(outlier)
    accumulated_charges = create_acc_charges(charges)
    saved_new_charge = save_new_charge(accumulated_charges, new_charge)
    print("saved new charge")
    print(saved_new_charge)
