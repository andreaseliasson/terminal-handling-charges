import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def compare_outlier_methods(charges, country_codes):
    """
    Use matlplot and seaborn to visualize how different outlier detection algorithms perform on the sample data.
    For now we are using percentile based and median absolute deviation based algorithms.
    After tuning some of the parameters and visualizing the result, it looks as if the percentile based algorithm
    is the better choice.
    :param charges: the sample charges
    :param country_codes: the country codes to loop over
    :return: Plots the data using seaborn
    """
    # Convert to pandas data frame for easier filtering
    charges_df = pd.DataFrame(charges)
    for country_code in country_codes:
        country_charges = charges_df[charges_df['port'].str.contains(r'^' + country_code)]
        values = np.array(country_charges['value'])
        plot(values, country_code)
    plt.show()


def mad_based_outlier(points, thresh=3.5):
    """
    Returns a boolean array with True if points are outliers and False otherwise.
    Based on code from a paper https://github.com/joferkington/oost_paper_code/blob/master/utilities.py
    :param points: An n by m array of charge values
    :param thresh: The modified z-score to use as a threshold. Observations with
        a modified z-score (based on the median absolute deviation) greater
        than this value will be classified as outliers.
    :return: n-length boolean array
    """
    # Returns boolean array indicating if point is an outlier or not
    if len(points.shape) == 1:
        points = points[:, None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh


def percentile_based_outlier(data, threshold=97.5):
    """
    Check if a given observation falls outside of the given threshold
    :param data: An n by m array of charge values
    :param threshold: the given percentile threshold to check against
    :return: n-length boolean array
    """
    # Returns boolean array indicating if point is an outlier or not
    diff = (100 - threshold) / 2.0
    min_val, max_val = np.percentile(data, [diff, 100 - diff])
    return (data < min_val) | (data > max_val)


def plot(values, country_code):
    """
    Use the seaborn library to plot the observations together with a kernel density estimation line
    for each outlier detection algorithm.
    :param values: An n by m array of charge values
    :param country_code: the given percentile threshold to check against
    :return: the actual plots
    """
    fig, axes = plt.subplots(nrows=2)
    for ax, func in zip(axes, [percentile_based_outlier, mad_based_outlier]):
        sns.distplot(values, ax=ax, rug=True, hist=False)
        outliers = values[func(values)]
        ax.plot(outliers, np.zeros_like(outliers), 'ro', clip_on=False)

    kwargs = dict(y=0.95, x=0.05, ha='left', va='top')
    axes[0].set_title('Percentile-based Outliers', **kwargs)
    axes[1].set_title('MAD-based Outliers', **kwargs)
    fig.suptitle('Comparing Outlier Tests for {} with n={} samples'.format(country_code, len(values)), size=14)


def get_outliers(values):
    """
    Gets the values of the charge outliers by using the percentile based outlier algorithm.
    :param values: An n by m array of charge values
    :return: n by m numpy array with the outlier values
    """
    outliers = values[percentile_based_outlier(values)]
    return outliers
