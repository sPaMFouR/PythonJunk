import pandas as pd
import numpy as np

precision = 4
limit = 1.0
file_name = 'radial'
list_columns = ['RA1', 'DEC1', 'RA2', 'DEC2']
data_df = pd.read_csv(file_name, header=None, names=list_columns, sep="\s+", engine='python')
rows = data_df.shape[0]

for index, row in data_df.iterrows():
    new_df = pd.DataFrame(index=(np.arange(0, 320, 1)))
    new_df['RA1'] = row['RA1']
    new_df['DEC1'] = row['DEC1']
    new_df.index.name = "STAR_ID"
    for idx in range(0, rows):
        val = ((row['RA1'] - data_df.loc[idx, 'RA2']) ** 2 + (row['DEC1'] - data_df.loc[idx, 'DEC2']) ** 2) ** 0.5
        if val > limit:
            new_df.loc[idx, 'RadDist'] = np.nan
        else:
            new_df.loc[idx, 'RadDist'] = val

    new_df = new_df.sort_values(by='RadDist').round(precision)

    data_df.loc[index, 'Distance'] = new_df['RadDist'].min()
    data_df.loc[index, 'ClosestRA'] = data_df.loc[new_df.iloc[0].name, 'RA2']
    data_df.loc[index, 'ClosestDEC'] = data_df.loc[new_df.iloc[0].name, 'DEC2']

    new_df.to_csv("File_" + str(index), sep=" ", index=True, header=True)

data_df = data_df.round(precision)
data_df.to_csv("OUTPUT_File", sep=" ", index=None, header=True)
print "Task Completed"
