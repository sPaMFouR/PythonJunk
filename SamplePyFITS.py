import pyfits
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fits_file = "nov17_afbs_ASASSN14dq-b1.fits"
fits_header = pyfits.getheader(fits_file)

print fits_header.keys()
print "Number Of Axes = " + str(fits_header['NAXIS'])
# One Image - 2 Axes
# Multiple Images - 3 Axes
# FITS Files Have Data In The Form Of A Data Cube

print "Size Of Image = {0} x {1}".format(str(fits_header['NAXIS1']), str(fits_header['NAXIS2']))

# print "Number Of Images = " + str(fits_header['NAXIS3'])

print "Is The Image Extended ? - " + str(fits_header['EXTEND'])

# print type(fits_header['NAXIS'])

file_data = pyfits.getdata(fits_file)
# plt.hist(file_data, bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.imshow(file_data, cmap=cm.gray, clim=(0.0, 1000))
plt.colorbar()
plt.savefig("image1.png")
plt.show()
plt.savefig("image2", format="png")  # If executed after plt.show(), nothing will be saved as the memory is flushed out
