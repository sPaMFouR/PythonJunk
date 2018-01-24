import glob
import pandas as pd
import os

os.chdir("/home/avinash/Downloads/")
list_files = glob.glob(pathname="file*.dcf")
list_cols = ['Mag1', 'Mag2', 'Mag3', 'Err1', 'Err2', 'Err3', 'Time']
dict_mean = {}
dict_std = {}

for file_name in list_files:
    file_df = pd.read_csv(filepath_or_buffer=file_name, names=list_cols, sep="\s+", engine='python')
    file_df.sort_values(by='Err1').sort_index(kind='mergesort')
    file_df = file_df[:20]
    dict_mean[file_name] = file_df['Err1'].mean()
    dict_std[file_name] = file_df['Err1'].std()

with open("Output_Log", 'w') as f:
    f.write("{0:>8} {1:>7} {2:>9}\n".format("FileName", "Mean", "Std"))
    for file_name in list_files:
        f.write("{0:>9} {1:>.5} {2:>.5}\n".format(file_name, dict_mean[file_name], dict_std[file_name]))


# This Code is not exactly what you want because i don't have the idea of the intricacies of the problem,
# but this will definitely solve the problem you are looking for with minor adjustments.

