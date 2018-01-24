import numpy as np
import matplotlib.pyplot as plt

#for loading the text file
x,y,v,color=np.loadtxt('ngc_104_Stars.txt', unpack=True)
count = 0
for i in range(0, len(x)):
	if 0.0<color[i]<0.5 and 14<v[i]<17:
		plt.plot(color[i],v[i],'c.')
              	count+= 1 
	else:
		plt.plot(color[i],v[i],'k.')

print count # number of selected points from the condtion

#labeling and ploting
plt.savefig('sneha_work.jpg')
plt.title("Sneha's Work")
plt.xlabel('B-V')
plt.ylabel('V')
plt.ylim(22,10)
plt.xlim(-0.5,2.5)
plt.show()

# for saving the if condition file 
f=open("BSS_ngc104.dat", "w")
for i in range(count):
	f.write(str("%10.4f" % x[i]) + "   " + str("%10.4f" % y[i]) + "   " + str("%10.4f" % v[i]) + "   " + str("%10.4f" % color[i]) + "\n")
f.close
