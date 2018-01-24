#!/usr/bin/python
# ------------------------------------------------------------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# ------------------------------------------------------------------------------------------------------------------- #

a02, b02, c02, d02, e02, f02, g02, h02, i02=np.genfromtxt('Tb_tmf_z7.08',unpack=True)

# ------------------------------------------------------------------------------------------------------------------- #

fig = plt.figure()
ax1 = plt.subplot(4, 4, 1)
l1 = plt.errorbar(a02, b02, yerr=f02/2, color='b', fmt='-', linewidth=1, label=r'$Z=7.08, X_{HI}=0.039725$')[0]

# ------------------------------------------------------------------------------------------------------------------- #

handles = [l1]
legend = fig.legend(handles, [r'$Z=7.08,~X_{HI}=0.039725$', '$Z=9.04,~ X_{HI}=0.442794$','$Z=18.32,~ X_{HI}=0.997475$'],
                    bbox_to_anchor=(0.5, 1), loc='upper center', ncol=3, prop={'size': 8.0}, fontsize='14')
legend.get_frame().set_linewidth(0.0)  # To remove box around legend

# ------------------------------------------------------------------------------------------------------------------- #

plt.axvline(x=0, color='black', linestyle='--', linewidth=0.5)  # For vertical grid line at a given location
plt.axhline(y=0.5, color='black', linestyle='--', linewidth=0.5)
plt.text(2, 0.1, r'$\delta T_{b}$', fontsize=12)
ax1.tick_params(width=0.2)  # For ticks thickness

ax1.set_ylim(0, 1)
ax1.set_ylabel(r'$\beta_{c}$')
ax1.yaxis.set_major_locator(FixedLocator(np.arange(0,1.25,0.25)))
ax1.yaxis.set_minor_locator(MultipleLocator(0.0625))
ax1.set_yticklabels(["0", "", "0.5", "", "1"])

ax1.set_xlim(-4, 4)
ax1.set_xlabel(r'$\nu$')
ax1.xaxis.set_major_locator(FixedLocator(range(-4,5,1)))
ax1.xaxis.set_minor_locator(MultipleLocator(0.25))
print ax1.get_xticks()
ax1.set_xticklabels(["-4", "", "-2", "", "0", "", "2", "", "4"])

plt.subplots_adjust(wspace=0.5, hspace=0.45)
plt.savefig("TMF_zeta50.eps", format="eps")
plt.show()

def set_plot_params(ax_obj, x_title, y_title,):

	ax_obj.set_ylim(0, 1)
	ax1.set_ylabel(r'$\beta_{c}$')
	ax1.yaxis.set_major_locator(FixedLocator(np.arange(0,1.25,0.25)))
	ax1.yaxis.set_minor_locator(MultipleLocator(0.0625))
	ax1.set_yticklabels(["0", "", "0.5", "", "1"])

	ax1.set_xlim(-4, 4)
	ax1.set_xlabel(r'$\nu$')
	ax1.xaxis.set_major_locator(FixedLocator(range(-4,5,1)))
	ax1.xaxis.set_minor_locator(MultipleLocator(0.25))
	ax1.set_xticklabels(["-4", "", "-2", "", "0", "", "2", "", "4"])

plt.axvline(x=0, color='black', linestyle='--', linewidth=0.5)  # For vertical grid line at a given location
plt.axhline(y=0.5, color='black', linestyle='--', linewidth=0.5)
plt.text(2, 0.1, r'$\delta T_{b}$', fontsize=12)
ax_obj.tick_params(width=0.2)  # For ticks thickness
plt.subplots_adjust(wspace=0.5, hspace=0.45)
plt.savefig("TMF_zeta50.eps", format="eps")
plt.show()

set_plot_params(ax_obj=ax1, xtitle='x', y_title='y')


