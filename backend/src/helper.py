import json
import pandas as pd
import numpy as np
from outlier_detection import get_outliers


def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def get_2_letter_country_codes(charges):
    unique_country_codes = set([charge['port'][:2] for charge in charges])
    return unique_country_codes


def get_country_charges_with_outliers(charges, country_codes):
    charges_df = pd.DataFrame(charges)

    accumulated_country_charges = []
    for country_code in country_codes:
        country_charges = charges_df[charges_df['port'].str.contains(r'^' + country_code)]
        values = np.array(country_charges['value'])
        outliers = get_outliers(values)
        accumulated_country_charges.append({'country_code': country_code,
                                            'values': values.tolist(),
                                            'outliers': list(outliers)})
    return accumulated_country_charges
