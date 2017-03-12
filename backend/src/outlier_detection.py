import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def compare_outlier_methods(charges, country_codes):
    # Convert to pandas data frame for easier filtering
    charges_df = pd.DataFrame(charges)
    for country_code in country_codes:
        country_charges = charges_df[charges_df['port'].str.contains(r'^' + country_code)]
        values = np.array(country_charges['value'])

        # Add three outliers for testing purposes
        # values = np.r_[values, -3, -10, 1000]
        plot(values, country_code)
    plt.show()


def mad_based_outlier(points, thresh=3.5):
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
    # Returns boolean array indicating if point is an outlier or not
    diff = (100 - threshold) / 2.0
    min_val, max_val = np.percentile(data, [diff, 100 - diff])
    return (data < min_val) | (data > max_val)


def plot(values, country_code):
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
    outliers = values[percentile_based_outlier(values)]
    return outliers
