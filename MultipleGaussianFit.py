import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy import optimize
import specutils.io.read_fits as spec
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


file_name = 'final_28aug.fits'
read_data = spec.read_fits_spectrum1d(str(file_name))
with fits.open(str(file_name)) as hdulist:
    image_data = hdulist[0].data
    image_hdr = hdulist[0].header

wav_data = read_data.dispersion
flux_data = image_data

majorLocator = MultipleLocator(200)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(10)

plt.plot(wav_data, flux_data)
plt.grid()
ax = plt.gca()
ax.xaxis.set_minor_locator(minorLocator)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
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
mean = sum(usable_wav) / length_data


def gaussian(x, height, center, width, offset):
    return height * np.exp(-(x - center) ** 2 / (2 * width ** 2)) + offset


def three_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, offset):
    return (gaussian(x, h1, c1, w1, offset=0) + gaussian(x, h2, c2, w2, offset=0) +
            gaussian(x, h3, c3, w3, offset=0) + offset)


def two_gaussians(x, h1, c1, w1, h2, c2, w2, offset):
    return three_gaussians(x, h1, c1, w1, h2, c2, w2, 0, 0, 1, offset)

# errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y) ** 2
# guess3 = [0.49, 0.55, 0.01, 0.6, 0.61, 0.01, 1, 0.64, 0.01, 0]
# I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope
# smoothness there
# optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:, 0], data[:, 1]))


def errfunc2(p, x, y):
    return (two_gaussians(x, *p) - y) ** 2

guess2 = [max(usable_flux), mean - 5, 1.0, 0.5 * max(usable_flux), mean + 5, 0.8, 0]
optim2, success = optimize.leastsq(func=errfunc2, x0=np.asarray(guess2), args=(usable_wav, usable_flux))[0:2]

plt.scatter(usable_wav, usable_flux, lw=5, c='g', label='Observed Spectra')
plt.plot(usable_wav, two_gaussians(usable_wav, *optim2), lw=3, c='b', label='Fit of 2 Gaussians')
plt.ylim(min(usable_flux) / 1.10, max(usable_flux) * 1.10)
plt.legend(loc='best')
plt.savefig('result.png')
plt.show()
