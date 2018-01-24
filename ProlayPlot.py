# --------------------------
# Import Modules
# --------------------------

import matplotlib.pyplot as plt
import os
import glob

# --------------------------
# Defining Global Variables
# --------------------------

obs_folder = '/home/prolay/Documents/progpelu/c/PhD/isochrones/data_even/'
theory_folder='/home/prolay/Documents/progpelu/c/PhD/isochrones/data_even/'
common_string_theory = 'smc_z13_out_*'
common_string_obs = 'subtiles_*'


# --------------------------
# Reading Observational data
# --------------------------

os.chdir(obs_folder)
list_obs_files = glob.glob(str(common_string_obs))
list_obs_files.sort()
list_obs_files = list_obs_files[0:9]


def read_obs_file(file_name):
    with open(file_name, 'r') as f:
        data_firstline = f.readline().split()
        data_list = f.read().split()
    
    columns = len(data_firstline)
    length_data = len(data_list)
    rows = length_data / columns
    
    mag_nuv = []
    mag_fuv = []
    mag_diff = []
    for i in range(0, rows):
        mag_nuv.append(float(data_list[6 + i * columns]))
        mag_fuv.append(float(data_list[8 + i * columns]))
        mag_diff.append(float(data_list[8 + i * columns]) - float(data_list[6 + i * columns]))
    
    return mag_fuv, mag_diff

# ------------------------
# Reading Theoretical Data
# ------------------------

os.chdir(theory_folder)
list_theory_files = glob.glob(str(common_string_theory))


def read_theory_file(file_name):
    with open(str(file_name),'r') as f:
        data_firstline = f.readline().split(',')
        data_list = []
        for line in f:
            data_line = line.split(',')
            data_list += data_line

    columns = len(data_firstline)
    length_data = len(data_list)
    rows = length_data / columns

    mag_nuv = []
    mag_fuv = []
    mag_diff = []

    age_galaxy = data_list[0]
    for i in range(0, rows):
        mag_nuv.append(float(data_list[26 + i * columns]))
        mag_fuv.append(float(data_list[25 + i * columns]))
        mag_diff.append(float(data_list[27 + i * columns]))

    return age_galaxy, mag_fuv, mag_diff

        
def plot_theory_file(file_name):
    age, mag_fuv, mag_diff = read_theory_file(str(file_name))
    plt.plot(mag_diff, mag_fuv, label=str(age))


def plot_obs_file(file_name):
    mag_fuv, mag_diff = read_obs_file(file_name)
    plt.scatter(mag_diff, mag_fuv, label='Obs_data')


def set_plot_params():
    ax = plt.gca()
    ax.invert_yaxis()
    plt.ylim(25, 10)
    plt.xlim(-1, 3)
    plt.legend(loc=1, fontsize=7)

plot_num = []
for i in range(1, 10):
        plot_num.append(int(str(3) + str(3) + str(i)))


for index in range(0, len(plot_num)):
    ax = plt.subplot(int(plot_num[index]))
    plot_obs_file(file_name=list_obs_files[index])
    for theory_files in list_theory_files:
        plot_theory_file(file_name=theory_files)
    set_plot_params()

plt.show()








