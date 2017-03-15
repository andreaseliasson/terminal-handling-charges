import pandas as pd
import numpy as np
import copy
from outlier_detection import get_outliers, percentile_based_outlier
from helper import dump_json
from normalize_currency import normalize_charge

ACCUMULATED_CHARGES_OUTPUT = '../data/accumulated_data.json'


def get_2_letter_country_codes(charges):
    unique_country_codes = set([charge['port'][:2] for charge in charges])
    return unique_country_codes


def get_country_charges_with_outliers(charges, country_codes):
    """
    Gets charges per country
    :param charges: the original sample charges
    :param country_codes: the set of unique job 2-letter country codes
    :return: list of charges with their country code, values and outliers
    """
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


def is_outlier(sample_charges, new_charge, currency_rates):
    """
    Naive way of checking if a new charge is an outlier by using the same algorithm we did when checking
    for the sample outliers. Based on exploring different outlier detection methods we will use the percentile
    based algorithm.
    :param sample_charges: the original sample charges
    :param new_charge: a new charge to check
    :param currency_rates: currency rates used to normalize value
    :return: Boolean indicating whether the new charge is an outlier
    """
    charges_df = pd.DataFrame(sample_charges)

    country_charges = charges_df[charges_df['port'].str.contains(r'^' + new_charge['port'][:2])]
    sample_values = np.array(country_charges['value'])

    # Normalize value to USD before feeding into the outlier detection
    normalized_new_charge = normalize_charge(new_charge, currency_rates)

    # Append new charge value
    values = np.append(sample_values, [normalized_new_charge['value']])

    # Check if last charge that we just appended is an outlier
    return percentile_based_outlier(values)[-1]


def save_new_charge(sample_charges, acc_charges, new_charge, currency_rates):
    """
    Save a new charge with a flag indicating if it's an outlier of it's ok (1 == outlier, 0 == ok).
    :param sample_charges: the original sample charges
    :param acc_charges: the accumulated charges to append the new charge to
    :param new_charge: new charge to add
    :param currency_rates: currency rates
    :return: new charge as a dict
    """
    # Add new property indicating whether or not the new charge is an outlier or not
    new_charge['outlier'] = int(is_outlier(sample_charges, new_charge, currency_rates))
    acc_charges.append(new_charge)

    # Dump list of dicts to a .json file for later references
    dump_json(acc_charges, ACCUMULATED_CHARGES_OUTPUT)

    return new_charge


def create_acc_charges(sample_charges):
    """
    Create accumulated charges to add new charges to. We wish to preserve the original sample charges.
    :param sample_charges: the original sample charges
    :return: the accumulated charges as deep copy of the original sample charges
    """
    accumulated_charges = copy.deepcopy(sample_charges)
    dump_json(accumulated_charges, ACCUMULATED_CHARGES_OUTPUT)
    return accumulated_charges
