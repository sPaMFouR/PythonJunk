import pandas as pd


def user_input(message, default):
    while True:
        try:
            user_value = int(raw_input("{0}(Default = {1}): ".format(message, default)) or str(default))
        except ValueError:
            print("\n*ERROR: The User Input Is Not A Number*\n")
        else:
            break
    return user_value


file_name = raw_input("Enter The Filename to Generate Time Series Data: ") or "uv_lightcurve.dat"

data_file = pd.read_csv(filepath_or_buffer=file_name, names=['Time', 'Mag1', 'Err1', 'Mag2', 'Err2'], sep="\s+",
                        engine='python')
rows = len(data_file.index.values)

delete_rows = user_input(message="Number Of Rows To Be Deleted?", default=10)
generate_files = user_input(message="Number Of Realisations To Be Implemented?", default=50)

while True:
    if delete_rows > rows:
        print("Failure To Perform Operation : You're Trying To Delete More Rows Than What The File Contains")
        delete_rows = user_input(message="Number Of Rows To Be Deleted?", default=10)
    else:
        break

format_mapping = {'Time': '{:.5f}', 'Mag1': '{:.5f}', 'Err1': '{:.5f}', 'Mag2': '{:.5f}', 'Err2': '{:.5f}'}

for index in range(1, generate_files + 1):
    new_df = data_file.sample(n=rows - delete_rows)
    new_df = new_df.sort_values(by='Time').sort_index(kind='mergesort')
    for key, value in format_mapping.items():
        new_df[key] = new_df[key].apply(value.format)

    new_df1 = new_df[['Time', 'Mag1', 'Err1']]
    new_df2 = new_df[['Time', 'Mag2', 'Err2']]

    new_df1.to_csv('file_{0}a.dat'.format(index), sep=" ", index=False, header=False)
    new_df2.to_csv('file_{0}b.dat'.format(index), sep=" ", index=False, header=False)
