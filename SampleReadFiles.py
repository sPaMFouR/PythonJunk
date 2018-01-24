
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
"""
with file("/home/avinash/Supernovae_Data/ASASSN14dq/Standards/PG0918/output_mag2", "r+") as f:
    for line in f:
        a,b,c,d,e,f,g,h,j,i,k,l,m = line.rstrip().split()

print a,b,c,d,e,f,g,h,i,j,k,l,m
"""

header = []
def xyz():
    total_elements1 = 0
    with file("/home/avinash/Supernovae_Data/ASASSN14dq/Standards/PG0918/output_mag2", "r+") as f:
        for i in range(0, 0):
            line = f.readline().rstrip()
            header.append(line.split())
        data_string = f.read()
        data_split1 = data_string.split()
        total_elements1 = len(data_split1)

    return total_elements1

print xyz()

"""
if any(not isinstance(y,(str)) for y in line):
                data_string = f.read()
                data_split = data_string.split()
                total_elements = len(data_split)
            count += 1
            """


"""
for line in f:
    print line

for line in f:
    print line, # To avoid the print statement using newline character
"""
x_val = []
y_val = []
z_val = []
with file("/home/avinash/Supernovae_Data/ASASSN14dq/Standards/PG0918/test", "r+") as f:
    for line in f:
        line = line.rstrip() # strip /t, /n, spaces from the right side
        x,y,z = line.split()
        x_val.append(float(x))
        y_val.append(float(y))
        z_val.append(float(z))
print x_val
print y_val
"""
for line in f:
    line = line.rstrip() # strip /t, /n, spaces from the right side
    print line
    x,y = line.split(",")
    print x, y
    x_val.append(float(x))
    y_val.append(float(y))
"""
"""
    "10" "," "100" "\n"

        temp=331+k
        plt.subplot(temp)
        plt.plot(x, y,  colors = 'g', linestyle = '-0', x, z, linestyle = colors_line[k])
#		plt.title(list_title[k])
        plt.xlabel(list_xlabel[k])
        plt.ylabel(list_ylabel[k])


plt.subtitle("Avinash")
header  = f.readline().rstrip().split()
"""


