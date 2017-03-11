import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def compare_outlier_methods(charges):
    charges_df = pd.DataFrame(charges)
    country = charges_df.loc[charges_df['currency'] == 'USD']
    values = np.array(country['value'])

    # Add three outliers for testing purposes
    values = np.r_[values, -3, -10, 1000]
    print(values)
    plot(values)

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


def plot(values):
    fig, axes = plt.subplots(nrows=2)
    for ax, func in zip(axes, [percentile_based_outlier, mad_based_outlier]):
        sns.distplot(values, ax=ax, rug=True, hist=False)
        print(func(values))
        outliers = values[func(values)]
        print('outliers')
        print(outliers)
        ax.plot(outliers, np.zeros_like(outliers), 'ro', clip_on=False)

    kwargs = dict(y=0.95, x=0.05, ha='left', va='top')
    axes[0].set_title('Percentile-based Outliers', **kwargs)
    axes[1].set_title('MAD-based Outliers', **kwargs)
    fig.suptitle('Comparing Outlier Tests with n={}'.format(len(values)), size=14)
