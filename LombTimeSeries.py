#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxx-------------------------SPECTRAL TIME SERIES ANALYSIS----------------------xxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# ------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# ------------------------------------------------------------------------------------------------------------------- #
import numpy as np
from matplotlib import pyplot as plt
from astroML.plotting import setup_text_plots
from astroML.time_series import lomb_scargle, lomb_scargle_BIC, lomb_scargle_bootstrap
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Read Data
# ------------------------------------------------------------------------------------------------------------------- #
file_1 = 'Macijewski_Tmid_O-C.dat'
with open(file_1, 'r') as fin:
    data_file = fin.read().split()

columns = 2
rows = len(data_file) / columns

list_time = []
list_diff = []

for index in range(0, rows):
    list_time.append(data_file[0 + index * columns])
    list_diff.append(data_file[1 + index * columns])

list_time = np.asarray(list_time, dtype=float)
list_diff = np.asarray(list_diff, dtype=float)

points = len(list_time)
dy = 0.5 + 0.5 * np.random.random(points)
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Compute Periodogram
# ------------------------------------------------------------------------------------------------------------------- #
min_period = (list_time[-1] - list_time[0]) / len(list_time)
max_period = list_time[-1] - list_time[0]
period = np.linspace(min_period, max_period, 10000)
omega = 2 * np.pi / period
PS = lomb_scargle(list_time, list_diff, dy, omega, generalized=True)
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Get Significance Via Bootstrap
# ------------------------------------------------------------------------------------------------------------------- #
D = lomb_scargle_bootstrap(list_time, list_diff, dy, omega, generalized=True, N_bootstraps=1000, random_state=0)
sig1, sig5 = np.percentile(D, [99, 95])
print sig1, sig5
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Plot The Results
# ------------------------------------------------------------------------------------------------------------------- #
fig = plt.figure(figsize=(5, 3.75))
fig.subplots_adjust(left=0.1, right=0.9, hspace=0.25)
setup_text_plots(fontsize=12, usetex=True)

# First panel: The Data

ax = fig.add_subplot(211)
ax.errorbar(list_time, list_diff, dy, fmt='ok', capsize=5, lw=1, ecolor='gray')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Flux')
ax.set_xlim(list_time[0] - 10, list_time[-1] + 10)

# Second panel: The Periodogram & Significance Levels

ax1 = fig.add_subplot(212, xscale='log')
ax1.plot(period, PS, '-', c='black', lw=1, zorder=1)
ax1.plot([period[0], period[-1]], [sig1, sig1], ':', c='black')
ax1.plot([period[0], period[-1]], [sig5, sig5], ':', c='black')

ax1.set_xlim(period[0], period[-1])
ax1.set_ylim(-0.05, 0.85)
ax1.set_xlabel(r'Period (days)')
ax1.set_ylabel('Power')
ax1.annotate("", (800, 0.3), (800, 0.8), ha='center', arrowprops=dict(arrowstyle='->'))

# Twin Axis: Label BIC On The Right Side

ax2 = ax1.twinx()
ax2.set_ylim(tuple(lomb_scargle_BIC(ax1.get_ylim(), list_diff, dy)))
ax2.set_ylabel(r'$\Delta BIC$')

ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
ax1.xaxis.set_minor_formatter(plt.FormatStrFormatter('%.0f'))
ax1.xaxis.set_major_locator(plt.LogLocator(10))

plt.show()
# ------------------------------------------------------------------------------------------------------------------- #

