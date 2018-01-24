#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxx--------------POLARISATION PLOT USING GALACTIC COORDINATES---------------xxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# ------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# ------------------------------------------------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Read Input File And Append XCos and XSin In The Pandas DataFrame
# ------------------------------------------------------------------------------------------------------------------- #
file_name = "isp_sgr.xlsx"
data_df = pd.read_excel(file_name)

for index, band in data_df['Pol'].iteritems():
    data_df.loc[index, r'XCos$\theta$'] = data_df.loc[index, 'Pol'] * np.cos(np.deg2rad(data_df.loc[index, 'PA']))
    data_df.loc[index, r'XSin$\theta$'] = data_df.loc[index, 'Pol'] * np.sin(np.deg2rad(data_df.loc[index, 'PA']))
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Plot The Polarisation Map Of NOVA Sgr
# ------------------------------------------------------------------------------------------------------------------- #
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

novasgr_x = data_df.loc[9, 'Glon']
novasgr_y = data_df.loc[9, 'Glat']
quiverpars = dict(color='b', headlength=0, headwidth=0, pivot='mid', headaxislength=0, scale=0.5, width=.01, units='xy')

ax.scatter(data_df['Glon'], data_df['Glat'], s=40, marker="*", color='k')
ax.quiver(data_df['Glon'], data_df['Glat'], data_df[r'XCos$\theta$'], data_df[r'XSin$\theta$'],  **quiverpars)
ax.text(s='NovaSGR', x=novasgr_x + 0.05, y=novasgr_y - 0.1, rotation="horizontal")

ax.set_xlim(3.0, 8.0)
ax.set_ylim(-11.0, -9.0)
ax.xaxis.set_ticks_position('both')
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.tick_params(which='both', direction='in', width=0.5, labelsize=10)
ax.set_xlabel("Galactic Longitude (Degrees)", fontsize=12)
ax.set_ylabel("Galactic Latitude (Degrees)", fontsize=12)

fig.savefig("OUTPUT_PlotRamGal.eps", format="eps")
plt.show()
plt.close(fig)
# ------------------------------------------------------------------------------------------------------------------- #
