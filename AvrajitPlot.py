##############################################################
#      PLOT HR Diagram By Reading Magnitudes From A File     #
##############################################################

import matplotlib.pyplot as plt

with open('fcatalogue.dat') as f:
    data_list=f.read().split()

vg = []
ig = []
vig = []

rows = 335

for i in range(0, rows):
	x = float(data_list[14 + i * 16])
    	y = float(data_list[15 + i * 16])
    	vg.append(x)
    	ig.append(y)
    	vig.append(x - y)
    	 
print vg, len(vg)
print ig, len(ig)
print vig, len(vig)

plt.scatter(vig, vg)
plt.ylim([30,10])
plt.xlim([-1,2])
plt.show()
