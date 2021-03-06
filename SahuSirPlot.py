# ------------------------------------------------------------------------------------------------------------------ #
# Import Required Libraries
# ------------------------------------------------------------------------------------------------------------------ #
import math
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Reads The File And Stores All The Values In A List "data_list"
# ------------------------------------------------------------------------------------------------------------------ #
with open("Cano_Table.dat") as f:
    temp_line = f.readline().split()
    data_list = f.read().split()
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Reads The File And Determines The No. Of Columns In The Data File
# ------------------------------------------------------------------------------------------------------------------ #
with open("Cano_Table.dat") as f:
    f.readline()
    f.readline()
    data_line = f.readline().split()

columns = len(data_line)
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Determines No. Of Rows In The Data File
# ------------------------------------------------------------------------------------------------------------------ #
length_data = len(data_list)
rows = length_data / columns
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Stores 'Ek' Values In A List For The Whole Data File
# ------------------------------------------------------------------------------------------------------------------ #
data_Ek = []
for i in range(0, rows):
    data_Ek.append(0.6 * float(data_list[8 + i * columns]))
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Splits 'Ek' Values Into Different Lists For Different Type Of Objects
# ------------------------------------------------------------------------------------------------------------------ #
data_Ek_GRB = data_Ek[0:20]
data_Ek_Ib = data_Ek[20:52]
data_Ek_Ic = data_Ek[52:61]
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Stores 'log_Ek' In A List For The Whole Data File
# ------------------------------------------------------------------------------------------------------------------ #
data_log_Ek = []
for i in range(0, rows):
    data_log_Ek.append(52 + math.log10(0.6 * float(data_list[8 + i * columns])))
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Splits 'log_Ek' Values Into Different Lists For Different Type Of Objects
# ------------------------------------------------------------------------------------------------------------------ #
data_log_Ek_GRB = data_log_Ek[0:20]
data_log_Ek_Ib = data_log_Ek[20:52]
data_log_Ek_Ic = data_log_Ek[52:61]
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Sorts The Lists[Not Really Required]
# ------------------------------------------------------------------------------------------------------------------ #
data_log_Ek_Ib.sort()
data_log_Ek_GRB.sort()
data_log_Ek_Ic.sort()
# ------------------------------------------------------------------------------------------------------------------ #

data_2014ad = 52 + math.log10(0.98)

# ------------------------------------------------------------------------------------------------------------------ #
# Creates Histogram Plots For Three Different Type Of Objects
# ------------------------------------------------------------------------------------------------------------------ #
counts1, bins1, patches1 = plt.hist(data_log_Ek_GRB, histtype='bar', log=False,
                                    bins=12, alpha=0.4, color='green', hatch="oo", label="GRB")
counts2, bins2, patches2 = plt.hist(data_log_Ek_Ib, histtype='bar', log=False,
                                    bins=13, alpha=0.4, color='black', hatch="--", label="Ib/c")
counts3, bins3, patches3 = plt.hist(data_log_Ek_Ic, histtype='bar', log=False,
                                    bins=8, alpha=0.4, color='red', hatch="\/", label="Ic-BL")

# Counts = Array Of Values Of The Histogram Bins
# Bins = Array Containing The Edges Of The Bins
# Patches = Silent List Of Individual Patches Used To Create Histogram
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Normalises The Above Histogram Plots
# ------------------------------------------------------------------------------------------------------------------ #
for item in patches1:
    item.set_height(item.get_height() / sum(counts1))
for item in patches2:
    item.set_height(item.get_height() / sum(counts2))
for item in patches3:
    item.set_height(item.get_height() / sum(counts3))
# ------------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------------------------ #
# Sets Plot Paramaters And Displays The Plot
# ------------------------------------------------------------------------------------------------------------------ #
# xvalues = [50.5, 51.0, 51.5, data_2014ad, 52.5, 53.0]
# xlabels = [50.5, 51.0, 51.5, "2014ad", 52.5, 53.0]
# plt.xticks(xvalues, xlabels, fontsize=10)
# plt.vlines(data_2014ad, 0, 0.5, label="2014ad")
plt.annotate('2014ad', xy=(data_2014ad, 0.23), xytext=(52.3, 0.30), arrowprops=dict(facecolor='blue', shrink=0.05))
plt.tick_params(axis='x', width=10, top="off")
plt.ylim((0, 0.5))
plt.xlabel('Kinetic Energy (Log $E_{kin}$)', fontsize=15)
plt.ylabel('No. Of Objects (Normalised)', fontsize=15)
plt.legend(prop={'size': 15})
plt.savefig("data_hist3.png")
plt.show()
# ------------------------------------------------------------------------------------------------------------------ #
