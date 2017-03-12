from flask import Flask
from flask import jsonify
from helper import load_json, get_2_letter_country_codes, get_country_charges_with_outliers
from normalize_currency import (get_unique_currencies,
                                get_currency_exchange_rates_from_api,
                                get_currency_exchange_rates_from_file,
                                normalize_charges)
from outlier_detection import compare_outlier_methods

app = Flask(__name__)


@app.route("/")
def start():
    charges = load_json('../data/sample_data.json')
    currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    normalized_charges = normalize_charges(charges, currency_rates)
    country_charges = get_country_charges_with_outliers(normalized_charges, get_2_letter_country_codes(charges))

    return jsonify(country_charges)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return response

if __name__ == "__main__":
    app.run()
    # charges = load_json('../data/sample_data.json')
    # unique_currencies = get_unique_currencies(charges)
    # # rates = get_currency_exchange_rates_from_api(unique_currencies)
    # currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    # normalized_charges = normalize_charges(charges, currency_rates)
    # country_charges = get_country_charges_with_outliers(normalized_charges, get_2_letter_country_codes(charges))
    #
    # # Distribution and outliers
    # # compare_outlier_methods(normalized_charges, get_2_letter_country_codes(charges))
