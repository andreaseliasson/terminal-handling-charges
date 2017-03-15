from flask import Flask
from flask import jsonify
from flask import request
from helper import load_json
from charges import (get_2_letter_country_codes,
                     get_country_charges_with_outliers,
                     create_acc_charges,
                     save_new_charge)
from normalize_currency import (get_unique_currencies,
                                get_currency_exchange_rates_from_api,
                                get_currency_exchange_rates_from_file,
                                normalize_charges)

app = Flask(__name__)


@app.route("/")
def start():
    charges = load_json('../data/sample_data.json')

    unique_currencies = get_unique_currencies(charges)
    currency_rates = get_currency_exchange_rates_from_api(unique_currencies)

    normalized_charges = normalize_charges(charges, currency_rates)
    country_charges = get_country_charges_with_outliers(normalized_charges, get_2_letter_country_codes(charges))

    return jsonify(country_charges)


@app.route('/charge', methods=['POST'])
def submit_new_charge():
    new_charge = request.json

    # Convert to correct types
    new_charge['value'] = float(new_charge['value'])
    new_charge['supplier_id'] = int(new_charge['supplier_id'])

    sample_charges = load_json('../data/sample_data.json')
    currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    normalized_sample_charges = normalize_charges(sample_charges, currency_rates)

    # Create an accumulator to hold new values as to not mutate the original sample data
    accumulated_charges = create_acc_charges(normalized_sample_charges)

    saved_new_charge = save_new_charge(normalized_sample_charges, accumulated_charges, new_charge, currency_rates)

    return jsonify(saved_new_charge)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return response

if __name__ == "__main__":
    app.run()
