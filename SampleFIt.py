import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import specutils.io.read_fits as spec
from matplotlib.ticker import MultipleLocator


file_name = 'final_28aug.fits'
read_data = spec.read_fits_spectrum1d(str(file_name))
with fits.open(str(file_name)) as hdulist:
    image_data = hdulist[0].data
    image_hdr = hdulist[0].header

wav_data = read_data.dispersion
flux_data = image_data

majorLocator = MultipleLocator(200)
minorLocator = MultipleLocator(10)

plt.plot(wav_data, flux_data)
plt.grid()
ax = plt.gca()
ax.xaxis.set_minor_locator(minorLocator)
ax.xaxis.set_major_locator(majorLocator)
ax.set_xlim(min(wav_data), max(wav_data))

ax2 = ax.twiny()
x_data = np.linspace(1, len(wav_data), len(ax.get_xticks()))
ax2.set_xticks(x_data)
plt.show()

pixel_range = raw_input("Enter The Pixel Range For The Line:").split(',')
lower_limit = int(pixel_range[0])
upper_limit = int(pixel_range[1])
usable_flux = flux_data[lower_limit:upper_limit]
usable_wav = wav_data[lower_limit:upper_limit]
usable_xdata = x_data[lower_limit:upper_limit]
length_data = len(usable_wav)
mean = sum(usable_wav) / length_data - 10


######################################
# Setting up test data
######################################


def norm(x, mean, sd):
    norm = []
    for i in range(x.size):
        norm += [1.0/(sd * np.sqrt(2 * np.pi)) * np.exp(-(x[i] - mean) ** 2/(2 * sd ** 2))]
    return np.array(norm)

mean1, mean2 = 0, -2
std1, std2 = 0.5, 1

x = np.linspace(-20, 20, 500)
y_real = norm(x, mean1, std1) + norm(x, mean2, std2)

######################################
# Solving
######################################

m, dm, sd1, sd2 = [5, 10, 1, 1]
p = [m, dm, sd1, sd2]  # [m, dm, sd1, sd2] Initial guesses for leastsq
y_init = norm(x, m, sd1) + norm(x, m + dm, sd2)  # For final comparison plot


def res(p, y, x):
    m, dm, sd1, sd2 = p
    m1 = m
    m2 = m1 + dm
    y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
    err = y - y_fit
    return err

plsq = leastsq(res, p, args=(y_real, x))

y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][0] + plsq[0][1], plsq[0][3])

plt.plot(x, y_real, label='Real Data')
plt.plot(x, y_init, 'r.', label='Starting Guess')
plt.plot(x, y_est, 'g.', label='Fitted')
plt.legend()
plt.show()
