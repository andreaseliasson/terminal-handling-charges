from flask import Flask
from read_json import load_json
from normalize_currency import (get_unique_currencies,
                                get_currency_exchange_rates_from_api,
                                get_currency_exchange_rates_from_file,
                                normalize_currencies)
app = Flask(__name__)


@app.route("/")
def start():
    return "Let's check for anomalies in terminal handling charges"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return response

if __name__ == "__main__":
    # app.run()
    charges = load_json('../data/sample_data.json')
    unique_currencies = get_unique_currencies(charges)
    # rates = get_currency_exchange_rates_from_api(unique_currencies)
    currency_rates = get_currency_exchange_rates_from_file('../data/currency_rates.json')
    normalized_charges = normalize_currencies(charges, currency_rates)
