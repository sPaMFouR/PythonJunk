import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

list_files = glob.glob("*.dat")
list_files.sort()
list_files += ["NaN"] * (30 - len(list_files) % 30)

list_temp = []
list_total = []
for file_name in list_files:
    list_temp.append(file_name)
    if len(list_temp) == 30:
        list_total.append(list_temp)
        list_temp = []

majorLocator = MultipleLocator(0.05)
minorLocator = MultipleLocator(0.01)


def plot_list(plot_num, list_files):
    fig, axes = plt.subplots(nrows=5, ncols=6)
    fig.tight_layout(w_pad=0.3, h_pad=0.2)
    for index, file_name in enumerate(list_files):
        if file_name != "NaN":
            data = np.loadtxt(file_name)
            ax = plt.subplot(5, 6, index + 1)
            ax.scatter(data[:, 0] - np.amin(data[:, 0]), data[:, 1], label=str(file_name.split(".")[0]), s=2)
            ax.legend(loc="upper right", fontsize=4)
            ax.set_xlabel("JD", fontsize=4)
            ax.set_ylabel("V Mag", fontsize=4)
            ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.xaxis.set_minor_locator(MultipleLocator(0.2))
            ax.yaxis.set_major_formatter(FormatStrFormatter("%4.2f"))
            ax.set_yticks(np.linspace(np.amin(data[:, 1]), np.amax(data[:, 1]) + 0.05, 5))

            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(4)
            for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(4)

    plt.savefig("Data_Set-" + str(plot_num + 1) + ".eps", format="eps", dpi=600)
    plt.close()

for plot_num, subset_list in enumerate(list_total):
    plot_list(plot_num, subset_list)
