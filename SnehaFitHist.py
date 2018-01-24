import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import MultipleLocator

file_name = 'sneha_data.csv'
data_df = pd.read_csv(file_name)
data_df = data_df[['mass', 'age', 'logt', 'logg']]


def gaussian_func(x, mean, sigma, const):
    return const * np.exp(-(x - mean) ** 2 / (sigma ** 2))


def dual_gaussian(x, mean1, sigma1, const1, mean2, sigma2, const2):
    return const1 * np.exp(-(x - mean1) ** 2 / (sigma1 ** 2)) + const2 * np.exp(-(x - mean2) ** 2 / (sigma2 ** 2))


plt.hist(data_df['mass'], bins=12)
plt.show()
plt.close()

hist, bins = np.histogram(data_df['mass'], bins=12)
width = 0.9 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2

plt.bar(center, hist, align='center', width=width)
plt.show()
plt.close()

mean, sigma = norm.fit(data_df['mass'])
print("Mean = {0}".format(mean))
print("Sigma = {0}".format(sigma))

fit = mlab.normpdf(bins, mean, sigma)
plt.bar(center, hist, align='center', width=width)
plt.plot(bins, fit, 'k--')
plt.show()
plt.close()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.set_title(r"$Mass\ of\ BSS\ : M\ = {0:.3f}, \sigma\ = {1:.3f}$".format(mean, sigma), fontsize=14)
ax.set_xlabel(r"$Mass (M_{\odot})$", fontsize=14)
ax.set_ylabel("No. Of Stars", fontsize=14)
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.tick_params(which='both', direction='in', labelsize=14)
ax.bar(center, hist, align='center', width=width)

popt, pcov = curve_fit(gaussian_func, center, hist)
ax.plot(center, gaussian_func(center, *popt), 'r--')
print("Single Gaussian Fit:")
print("Optimised Parameters = {0}\n".format(popt))

popt1, pcov1 = curve_fit(dual_gaussian, center, hist)
ax.plot(center, dual_gaussian(center, *popt1), 'k--')
print("Dual Gaussian Fit:")
print("Optimised Parameters = {0}\n".format(popt1))


plt.show()
plt.close(fig)