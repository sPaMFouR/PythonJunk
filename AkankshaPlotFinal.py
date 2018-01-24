#!/usr/bin/python
# ------------------------------------------------------------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, MultipleLocator

# ------------------------------------------------------------------------------------------------------------------- #

HOME_DIR = "/home/akanksha/Reionization/TMF/stephen2D_ver4/results_MFs/zeta50/smooth4.5/"

# a01,b01,c01,d01,e01,f01,g01,h01,i01=np.genfromtxt(HOME_DIR + 'Tb_tmf_z6.03',unpack=True)
# a03,b03,c03,d03,e03,f03,g03,h03,i03=np.genfromtxt(HOME_DIR + 'Tb_tmf_z8.09',unpack=True)
# a05,b05,c05,d05,e05,f05,g05,h05,i05=np.genfromtxt(HOME_DIR + 'Tb_tmf_z11.99',unpack=True)
# a11,b11,c11,d11,e11,f11,g11,h11,i11=np.genfromtxt(HOME_DIR + 'Ts_tmf_z6.03',unpack=True)
# a13,b13,c13,d13,e13,f13,g13,h13,i13=np.genfromtxt(HOME_DIR + 'Ts_tmf_z8.09',unpack=True)
# a15,b15,c15,d15,e15,f15,g15,h15,i15=np.genfromtxt(HOME_DIR + 'Ts_tmf_z11.99',unpack=True)
# a21,b21,c21,d21,e21,f21,g21,h21,i21=np.genfromtxt(HOME_DIR + 'delta_tmf_z6.03',unpack=True)
# a23,b23,c23,d23,e23,f23,g23,h23,i23=np.genfromtxt(HOME_DIR + 'delta_tmf_z8.09',unpack=True)
# a25,b25,c25,d25,e25,f25,g25,h25,i25=np.genfromtxt(HOME_DIR + 'delta_tmf_z11.99',unpack=True)
# a31,b31,c31,d31,e31,f31,g31,h31,i31=np.genfromtxt(HOME_DIR + 'xh_tmf_z6.03',unpack=True)
# a33,b33,c33,d33,e33,f33,g33,h33,i33=np.genfromtxt(HOME_DIR + 'xh_tmf_z8.09',unpack=True)
# a35,b35,c35,d35,e35,f35,g35,h35,i35=np.genfromtxt(HOME_DIR + 'xh_tmf_z11.99',unpack=True)

a02, b02, c02, d02, e02, f02, g02, h02, i02 = np.genfromtxt(HOME_DIR + 'Tb_tmf_z7.08', unpack = True)
a04, b04, c04, d04, e04, f04, g04, h04, i04 = np.genfromtxt(HOME_DIR + 'Tb_tmf_z9.04', unpack = True)
a06, b06, c06, d06, e06, f06, g06, h06, i06 = np.genfromtxt(HOME_DIR + 'Tb_tmf_z18.32', unpack = True)
a12, b12, c12, d12, e12, f12, g12, h12, i12 = np.genfromtxt(HOME_DIR + 'Ts_tmf_z7.08', unpack = True)
a14, b14, c14, d14, e14, f14, g14, h14, i14 = np.genfromtxt(HOME_DIR + 'Ts_tmf_z9.04', unpack = True)
a16, b16, c16, d16, e16, f16, g16, h16, i16 = np.genfromtxt(HOME_DIR + 'Ts_tmf_z18.32', unpack = True)
a22, b22, c22, d22, e22, f22, g22, h22, i22 = np.genfromtxt(HOME_DIR + 'delta_tmf_z7.08', unpack = True)
a24, b24, c24, d24, e24, f24, g24, h24, i24 = np.genfromtxt(HOME_DIR + 'delta_tmf_z9.04', unpack = True)
a26, b26, c26, d26, e26, f26, g26, h26, i26 = np.genfromtxt(HOME_DIR + 'delta_tmf_z18.32', unpack = True)
a32, b32, c32, d32, e32, f32, g32, h32, i32 = np.genfromtxt(HOME_DIR + 'xh_tmf_z7.08', unpack = True)
a34, b34, c34, d34, e34, f34, g34, h34, i34 = np.genfromtxt(HOME_DIR + 'xh_tmf_z9.04', unpack = True)
a36, b36, c36, d36, e36, f36, g36, h36, i36 = np.genfromtxt(HOME_DIR + 'xh_tmf_z18.32', unpack=True)

# ------------------------------------------------------------------------------------------------------------------- #

fig = plt.figure()
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.5)
plt.axhline(y=0.5, color='black', linestyle='--', linewidth=0.5)


def set_plot_params(ax_obj, x_title, y_title, text, plot_err):
    ax_obj.set_ylim(0, 1)
    ax_obj.set_ylabel(y_title)
    ax_obj.yaxis.set_major_locator(FixedLocator(np.arange(0, 1.25, 0.25)))
    ax_obj.yaxis.set_minor_locator(MultipleLocator(0.0625))
    ax_obj.set_yticklabels(["0", "", "0.5", "", "1"])

    ax_obj.set_xlim(-4, 4)
    ax_obj.set_xlabel(x_title)
    ax_obj.xaxis.set_major_locator(FixedLocator(np.arange(-4, 5, 1)))
    ax_obj.xaxis.set_minor_locator(MultipleLocator(0.25))
    ax_obj.set_xticklabels(["-4", "", "-2", "", "0", "", "2", "", "4"])
    ax_obj.tick_params(width=0.2)

    ax_obj.text(2, 0.1, text, fontsize=12)
    ax_obj.errorbar(plot_err[0][0], plot_err[0][1], yerr=plot_err[0][2] / 2, color='b', fmt='-', linewidth=1)
    ax_obj.errorbar(plot_err[1][0], plot_err[1][1], yerr=plot_err[1][2] / 2, color='c', fmt='-', linewidth=1)
    ax_obj.errorbar(plot_err[2][0], plot_err[2][1], yerr=plot_err[2][2] / 2, color='indianred', fmt='-', linewidth=1)

# ------------------------------------------------------------------------------------------------------------------- #

l1 = plt.errorbar(a02, b02, yerr=f02/2, color='b', fmt='-', linewidth=1, label=r'$Z=7.08, X_{HI}=0.039725$')[0]
l2 = plt.errorbar(a04, b04, yerr=f04/2, color='c', fmt='-', linewidth=1, label=r'$Z=9.04, X_{HI}=0.442794$')[0]
l3 = plt.errorbar(a06, b06, yerr=f06/2, color='indianred', fmt='-', linewidth=1, label=r'$Z=18.32, X_{HI}=0.997475$')[0]

handles = [l1, l2, l3]
legend = fig.legend(handles, [r'$Z=7.08,\ X_{HI}=0.039725$', '$Z=9.04,\ X_{HI}=0.442794$',
                              '$Z=18.32,\ X_{HI}=0.997475$'], bbox_to_anchor=(0.5, 1),
                    loc='upper center', ncol=3, prop={'size': 8.0}, fontsize='14')
legend.get_frame().set_linewidth(0.0)  # To remove box around legend

# ------------------------------------------------------------------------------------------------------------------- #

xlabel = r'$\nu$'
list_ylabels = [r'$\beta_{c}$', r'$\beta_{h}$', r'$\beta$', r'$\alpha$']
list_text = [r'$\delta T_{b}$', r'$T_{s}$', r'$\delta_{nl}$', r'$x_{HI}$']

list_ploterrs = [[[a02, b02, f02], [a04, b04, f04], [a06, b06, f06]],
                 [[a02, c02, g02], [a04, c04, g04], [a06, c06, g06]],
                 [[a02, d02, h02], [a04, d04, h04], [a06, d06, h06]],
                 [[a02, e02, i02], [a04, e04, i04], [a06, e06, i06]],
                 [[a12, b12, f12], [a14, b14, f14], [a16, b16, f16]],
                 [[a12, c12, g12], [a14, c14, g14], [a16, c16, g16]],
                 [[a12, d12, h12], [a14, d14, h14], [a16, d16, h16]],
                 [[a12, e12, i12], [a14, e14, i14], [a16, e16, i16]],
                 [[a22, b22, f22], [a24, b24, f24], [a26, b26, f26]],
                 [[a22, c22, g22], [a24, c24, g24], [a26, c26, g26]],
                 [[a22, d22, h22], [a24, d24, h24], [a26, d26, h26]],
                 [[a22, e22, i22], [a24, e24, i24], [a26, e26, i26]],
                 [[a32, b32, f32], [a34, b34, f34], [a36, b36, f36]],
                 [[a32, c32, g32], [a34, c34, g34], [a36, c36, g36]],
                 [[a32, d32, h32], [a34, d34, h34], [a36, d36, h36]],
                 [[a32, e32, i32], [a34, e34, i34], [a36, e36, i36]]]

for index in range(0, 16, 1):
    set_plot_params(fig.add_subplot(4, 4, index + 1), xlabel, list_ylabels[index % 4], list_text[index / 4],
                    list_ploterrs[index])

plt.subplots_adjust(wspace=0.5,hspace=0.45)
plt.savefig("TMF_zeta50.eps", format="eps")
plt.show()

# ------------------------------------------------------------------------------------------------------------------- #
