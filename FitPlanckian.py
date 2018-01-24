#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxx-----------------Fit Planckian Function To A Spectrum---------------xxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #


# -------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# -------------------------------------------------------------------------------------------------------------------- #
import pylab as plt
import numpy as np
from scipy.constants import h, k, c
from scipy.optimize import curve_fit
from PyAstronomy.pyasl import planck
# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Functions
# -------------------------------------------------------------------------------------------------------------------- #
def blackbody_flux(wave, temp):
    """
    Calculates blackbody flux as a function of wavelength (um) and temperature (K).
    Args:
        wave    : Wavelength (In Angstroms)
        temp    : Temperature (In Kelvin)
    Returns:
         units of erg/s/cm^2/cm/Steradian
    """
    wave = np.asarray(wave)
    wave *= 1e-10
    return 2 * np.pi * h * c**2 / ((wave ** 5) * (np.exp(h * c / (wave * k * temp)) - 1))


def file_to_csv(file_name):
    """
    Converts files containing tabular data to a csv(comma separated value) file.
    Args:
        file_name  : Text file which has to be converted
    Returns:
        None
    """
    with open(str(file_name), 'r') as fin:
        data_line = fin.readline().split()
        data_list = fin.read().split()
        columns = len(data_line)
        length_data = len(data_list)
        rows = length_data / columns
        data_list = data_line + data_list

    wave = []
    flux = []

    for index in range(0, rows):
        wave.append(float(data_list[0 + index * columns]))
        flux.append(float(data_list[1 + index * columns]))

    flux = [(value / float(np.mean(flux))) - 1. for value in flux]

    with open(str(file_name).rsplit('.')[0] + '.csv', 'w') as fout:
        fout.write('wavelog_input,flatflux_input,flatflux_err_input,flatflux_input_sm' + '\n')
        for index in range(0, rows):
            fout.write("%9.4f" % wave[index] + ',' + "%6.4f" % flux[index] + ',0.001,0.001' + '\n')

    return str(file_name).rsplit('.')[0] + '.csv'


def read_columns(file_name, column_indices, delimiter=','):
    """
    Reads columns mentioned by the indexes in the list 'column_indices' from file 'file_name' and returns a list
    of those columns.
    Args:
        file_name       : Text file which has to be read
        column_indices  : List of indexes of columns to be extracted
        delimiter       : Type of delimiter used in the file
    Returns:
        list_columns    : List of the extracted columns (Each column is a sub_list)
    """
    with open(str(file_name), 'r') as fin:
        columns = len(fin.readline().split(str(delimiter)))
        data_matrix = []
        for line in fin:
            data_matrix += line.strip().split(str(delimiter))
        rows = len(data_matrix) / columns
    
    list_columns = []
    for value in column_indices:
        temp_list = []
        for index in range(0, rows):
            temp_list.append(float(data_matrix[value + index * columns]))
        list_columns.append(temp_list)

    return list_columns

# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Location Of Directories And Files
# -------------------------------------------------------------------------------------------------------------------- #
file_name1 = '10qts_20100815_Lick_3-m_v1-z.flm-flat.csv'
file_name2 = '2002ap_HST_STIS_20020201.dat'
file_name3 = '2002ap_20020202_4000_7498_00.dat'
file_name4 = '2004aw-20040321.flm'
file_name5 = 'sn2002ap-20020206.flm'
# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Function For Plotting
# -------------------------------------------------------------------------------------------------------------------- #
[wave_data, flux_data] = read_columns(file_name=file_to_csv(file_name5), column_indices=[0, 1], delimiter=',')

Temp_1 = 6000.
Temp_2 = 7000.
y1 = blackbody_flux(wave_data, Temp_1)
y2 = blackbody_flux(wave_data, Temp_2)
sigma = np.std(wave_data)
ytot = y1 + y2

print h, k, c
print np.mean(flux_data)
print np.mean(y1)
# -------------------------------------------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------------------------------------------- #
# Plot the input model and synthetic data
# -------------------------------------------------------------------------------------------------------------------- #

plt.figure()
plt.plot(wave_data, y1, ':', lw=2, label='Temp_1 = %.0f' % Temp_1)
plt.plot(wave_data, y2, ':', lw=2, label='Temp_2 = %.0f' % Temp_2)
plt.plot(wave_data, ytot, ':', lw=2, label='Temp_1 + Temp_2\n(True Model)')
plt.plot(wave_data, flux_data, ls='steps-mid', lw=2, label='Observed Data')
plt.xlabel('Wavelength (Microns)')
plt.ylabel('Intensity (erg/s/cm$^2$/cm/Steradian)')

# fit two blackbodies to the synthetic data
# Note the initial guess values for Temp_1 and Temp_2 (p0 keyword below). They
# are quite different to the known true values, but not *too*
# different. If these are too far away from the solution curve_fit()
# will not be able to find a solution. This is not a Python-specific
# problem, it is true for almost every fitting algorithm for
# non-linear models. The initial guess is important!


def func(wave_list, temp_1, temp_2):
    return blackbody_flux(wave_list, temp_1) + blackbody_flux(wave_list, temp_2)

popt, pcov = curve_fit(func, wave_data, flux_data, p0=[1000, 3000], sigma=sigma)

bestTemp_1, bestTemp_2 = popt
sigmaTemp_1, sigmaTemp_2 = np.sqrt(np.diag(pcov))

ybest = blackbody_flux(wave_data, bestTemp_1) + blackbody_flux(wave_data, bestTemp_2)

print 'Initial Values:'
print '  Temp_1 = %.2f' % Temp_1
print '  Temp_2 = %.2f' % Temp_2

print '\nBest-Fitting Model Parameters:'
print '  Temp_1 = %.2f +/- %.2f' % (bestTemp_1, sigmaTemp_1)
print '  Temp_2 = %.2f +/- %.2f' % (bestTemp_2, sigmaTemp_2)

degrees_of_freedom = len(wave_data) - 2
resid = (flux_data - func(wave_data, *popt)) / sigma
chisq = np.dot(resid, resid)

print '\nDegrees Of Freedom =', degrees_of_freedom
print 'Chi-Squared = %.2f' % chisq
print 'Normalised Chi-Squared = %.2f' % float(chisq / degrees_of_freedom)


plt.plot(wave_data, ybest, label='Best Fitting\nModel')
plt.legend(frameon=False)
plt.savefig('fit_bb.png')
plt.show()
