#Reading the file
with open('test4', 'r') as f1:
    data=f1.read()

#Making a list of elements in the data file
data_list = data.split()
length_of_data = len(data_list)

#Input the value of tau
tau_string = int(raw_input("Enter the value of tau:"))

#Generare two columns based on the value of tau
column1 = data_list[0:length_of_data - tau]
column2 = data_list[tau:length_of_data]
total_elements = len(column1)

#Finally write the columns onto the output file
with open("test5", "w") as f2:
    for i in range(total_elements):
        f2.write(str(column1[i]) + " " + str(column2[i]) + "\n")

