#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# ------------------------------------------------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Reading Data And Sorting Values
# ------------------------------------------------------------------------------------------------------------------- #
file_name = "sky_data.xlsx"
data_df = pd.read_excel(file_name, header=None)
data_df = data_df.sort_values(by=0)
data_df = data_df.reset_index(drop=True)
data_df = data_df[[0, 1, 12]]
data_df.columns = ['X', 'Y', 'Z']
data_df.to_excel("sky_out.xlsx")
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Generate 2D Array For Contour Plot
# ------------------------------------------------------------------------------------------------------------------- #
x = data_df['X']
y = data_df['Y']
z = data_df['Z']

xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
xi, yi = np.meshgrid(xi, yi)
zi = interp.griddata((x, y), z, (xi, yi), method='cubic')
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Plot Filled Contour Plots With Continuous Color Map
# ------------------------------------------------------------------------------------------------------------------- #

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

colors = ['red', 'brown', 'yellow', 'green', 'blue']
cmap = LinearSegmentedColormap.from_list('name', colors)
norm = plt.Normalize(-1.3, -0.8)

ax.set_xlabel("X($^{\circ}$)", fontsize=12)
ax.set_ylabel("Y($^{\circ}$)", fontsize=12)
ax.set_title('OGLE III Map - IV')
ax.set_ylim(-2.4, 1.8)
ax.set_xlim(-2.4, 2.3)
ax.contour(xi, yi, zi, 8, cmap=cmap, norm=norm)
im = plt.imshow(zi, vmin=z.min(), vmax=z.max(), cmap=cmap, norm=norm, origin='lower',
                extent=[x.min(), x.max(), y.min(), y.max()])

fig.colorbar(im)
fig.savefig("OUTPUT_PlotFilledContour.eps", format='eps')
plt.show()
plt.close(fig)

# ------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------------------------------------------------------------------- #
# Plot Line Contour With Discrete ColorBars
# ------------------------------------------------------------------------------------------------------------------- #
fig2 = plt.figure(figsize=(10, 8))
ax = fig2.add_subplot(111)

ax.set_xlabel("X($^{\circ}$)", fontsize=12)
ax.set_ylabel("Y($^{\circ}$)", fontsize=12)
ax.set_title('OGLE III Map - IV')
ax.set_ylim(-2.4, 1.8)
ax.set_xlim(-2.4, 2.3)

colors = ['red', 'brown', 'yellow', 'green', 'blue']
cmap = LinearSegmentedColormap.from_list('name', colors)
norm = plt.Normalize(-1.3, -0.8)
bounds = [-0.7, -0.8, -0.9, -1.0, -1.1, -1.2]

im = plt.contour(xi, yi, zi, 8, cmap=cmap, norm=norm)
cbar = fig2.colorbar(im, ticks=[-0.7,-0.8,-0.9,-1.0,-1.1,-1.2])
cbar.ax.set_yticklabels(['-0.7', '-0.8', '-0.9', '-1.0', '-1.1', '-1.2'])

fig2.savefig("OUTPUT_PlotLineContour.eps", format='eps')
plt.show()
plt.close(fig2)
# ------------------------------------------------------------------------------------------------------------------- #


# NOTE: This Doesn't Work Properly. Have To Edit It For Discrete ColorBar
# ------------------------------------------------------------------------------------------------------------------- #
# Plot Line Contour Plot With Discrete ColorBars
# ------------------------------------------------------------------------------------------------------------------- #
fig3 = plt.figure(figsize=(10, 8))
ax = fig3.add_subplot(111)

ax.set_xlabel("X($^{\circ}$)", fontsize=12)
ax.set_ylabel("Y($^{\circ}$)", fontsize=12)
ax.set_title('OGLE III Map - IV')
ax.set_ylim(-2.4, 1.8)
ax.set_xlim(-2.4, 2.3)

cmap = ListedColormap(['red', 'brown', 'yellow', 'green', 'blue', 'cyan'])
norm = plt.Normalize(-1.3, -0.8)
bounds = [-0.7, -0.8, -0.9, -1.0, -1.1, -1.2]

# norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
im = plt.contour(xi, yi, zi, 8, cmap=cmap, norm=norm)
heatmap = ax.pcolor(zi, cmap=cmap)
cbar = plt.colorbar(heatmap)
im = plt.imshow(zi, vmin=z.min(), vmax=z.max(), cmap=cmap, norm=norm, origin='lower', extent=[x.min(), x.max(), y.min(), y.max()])
# cbar = fig2.colorbar(im, ticks=[-0.7,-0.8,-0.9,-1.0,-1.1,-1.2])
# cbar.ax.set_yticklabels(['-0.7', '-0.8', '-0.9', '-1.0', '-1.1', '-1.2'])
fig3.savefig("OUTPUT_PlotLineContour2.eps", format='eps')
plt.show()
plt.close(fig3)
# ------------------------------------------------------------------------------------------------------------------- #
