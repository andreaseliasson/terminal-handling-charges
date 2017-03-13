import pandas as pd
import numpy as np
import copy
from outlier_detection import get_outliers, percentile_based_outlier
from helper import dump_json

ACCUMULATED_CHARGES_OUTPUT = '../data/accumulated_data.json'


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


# Naive way of re-using the existing logic to check for outliers with new charge included
# Not very efficient
def is_outlier(sample_charges, new_charge):
    charges_df = pd.DataFrame(sample_charges)

    country_charges = charges_df[charges_df['port'].str.contains(r'^' + new_charge['port'][:2])]
    sample_values = np.array(country_charges['value'])

    # Append new charge value
    values = np.append(sample_values, [new_charge['value']])

    # Check if last charge that we just appended is an outlier
    return percentile_based_outlier(values)[-1]


def save_new_charge(sample_charges, acc_charges, new_charge):
    # Add new property indicating whether or not the new charge is an outlier or not
    new_charge['outlier'] = int(is_outlier(sample_charges, new_charge))
    acc_charges.append(new_charge)

    # Dump list of dicts to a .json file for later references
    dump_json(acc_charges, ACCUMULATED_CHARGES_OUTPUT)

    return new_charge


def create_acc_charges(sample_charges):
    accumulated_charges = copy.deepcopy(sample_charges)
    dump_json(accumulated_charges, ACCUMULATED_CHARGES_OUTPUT)
    return accumulated_charges
