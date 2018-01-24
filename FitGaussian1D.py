#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxx-----------------GAUSSIAN FITTING OF 1-D SPECTRA---------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #


# -------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# -------------------------------------------------------------------------------------------------------------------- #
import numpy
from astropy.io import fits
import PyAstronomy.pyasl as psl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import specutils.io.read_fits as spec
from matplotlib.ticker import MultipleLocator
# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Function For Plotting
# -------------------------------------------------------------------------------------------------------------------- #

def plot_data(x_array, y_array):
    fig = plt.figure()
    ax = plt.gca()
    ax.plot(x_array, y_array)
    major_locator = MultipleLocator(200)
    minor_locator = MultipleLocator(10)
    ax.xaxis.set_minor_locator(minor_locator)
    ax.xaxis.set_major_locator(major_locator)
    ax.set_xlim(min(x_array) - 50, max(x_array) + 50)
    ax.grid()

    return fig, ax

# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Read 1-D Spectra
# -------------------------------------------------------------------------------------------------------------------- #

# file_name = 'cfwcbs_ASASSN14dq-gr7.ms.fits'
file_name = 'final_28aug.fits'
read_data = spec.read_fits_spectrum1d(str(file_name))
with fits.open(str(file_name)) as hdulist:
    image_data = hdulist[0].data
    image_hdr = hdulist[0].header

wav_data = read_data.dispersion
flux_data = image_data

# print type(image_data), image_data.shape
# print read_data[0].dispersion
# print len(read_data[0].dispersion), len(list(read_data[0]))
# image_hdr2 = fits.getheader('fwcbs_ASASSN14dq-gr7.ms.fits')
# print image_data.shape, len(list(read_data.dispersion))
# init_value = image_hdr['CRVAL1']
# step_size = image_hdr['CD1_1']
# wav_array, flux_array = psl.read1dFitsSpec(fn=file_name, hdu=0)
# plot_data(x_array=wav_data, y_array=flux_data)
# plt.show()
# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# View 1-D Spectra
# -------------------------------------------------------------------------------------------------------------------- #
wav_array, flux_array = psl.read1dFitsSpec(fn=file_name, hdu=0)
fig, ax = plot_data(x_array=wav_data, y_array=flux_data)
ax2 = ax.twiny()
ax2.set_xticks(numpy.linspace(1, len(wav_data), len(ax.get_xticks())))
plt.show()

pixel_range = raw_input("Enter The Pixel Range For The Line (X, Y): ").split(',')
lower_limit = int(pixel_range[0])
upper_limit = int(pixel_range[1])

usable_flux = flux_data[lower_limit:upper_limit]
usable_wav = wav_data[lower_limit:upper_limit]
length_data = len(usable_wav)

mean = sum(usable_wav) / length_data
amp = max(usable_flux)
sigma = numpy.std(usable_wav) * 0.7
# sigma = (sum(usable_flux * (usable_wav - mean) ** 2)) ** 0.5


def gaussian_func(wav, mean_wav, sigma_wav, const):
    return const * numpy.exp(-(wav - mean_wav) ** 2 / (sigma_wav ** 2))


popt, pcov = curve_fit(gaussian_func, usable_wav, usable_flux, p0=[mean, sigma, amp])
plt.plot(usable_wav, gaussian_func(usable_wav, *popt))
print "Optimal Parameters For The Gaussian Fit : {0}".format(popt)
plt.scatter(usable_wav, usable_flux)
plt.show()

# -------------------------------------------------------------------------------------------------------------------- #

