#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxx---------------------------PLOT 1-D SPECTRA (PAVANA)--------------------------xxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# ------------------------------------------------------------------------------------------------------------------- #
# Import Required Libraries
# ------------------------------------------------------------------------------------------------------------------- #
import os
import re
import glob
from astropy.io import fits
import matplotlib.pyplot as plt
import specutils.io.read_fits as spec
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Functions For File Handling
# ------------------------------------------------------------------------------------------------------------------- #

def remove_file(file_name):
    """
    Removes the file "file_name" in the constituent directory.
    Args:
         file_name  : Name of the file to be removed from the current directory
    Returns:
        None
    """
    try:
        os.remove(file_name)
    except OSError:
        pass


def remove_similar_files(common_text):
    """
    Removes similar files based on the string "common_text".
    Args:
        common_text : String containing partial name of the files to be deleted
    Returns:
        None
    """
    for residual_files in glob.glob(common_text):
        os.remove(residual_files)


def group_similar_files(text_list, common_text, exceptions=''):
    """
    Groups similar files based on the string "common_text". Writes the similar files
    onto the list 'text_list' (only if this string is not empty) and appends the similar
    files to a list 'python_list'.
    Args:
        text_list   : Name of the output text file with names grouped based on the 'common_text'
        common_text : String containing partial name of the files to be grouped
        exceptions  : String containing the partial name of the files that need to be excluded
    Returns:
        list_files  : Python list containing the names of the grouped files
    """
    list_files = glob.glob(common_text)
    if exceptions != '':
        list_exception = exceptions.split(',')
        for file_name in glob.glob(common_text):
            for text in list_exception:
                test = re.search(str(text), file_name)
                print file_name
                if test:
                    try:
                        list_files.remove(file_name)
                    except ValueError:
                        pass

    list_files.sort()
    if len(text_list) != 0:
        with open(str(text_list), "w") as f:
            for index in range(0, len(list_files)):
                f.write(str(list_files[index]) + "\n")

    return list_files


def text_list_to_python_list(text_list):
    """
    Returns data in the file 'text_list' as a python_list.
    Args:
        text_list   : Input file containing filenames
    Returns:
        python_list : List of all the elements in the file 'text_list'
    Raises:
        Error : File 'text_list 'Not Found
    """
    if os.path.isfile(text_list):
        with open(text_list, "r+") as f:
            python_list = f.read().split()
            return python_list
    else:
        print "Error : File " + str(text_list) + " Not Found"


def python_list_to_text_list(python_list, text_list):
    """
    Put the data from the input 'python_list' to a file 'text_list' line-wise.
    Args:
        python_list : Python_list from which data has to be read
        text_list   : Name of the text file onto which data has to be appended
    Returns:
        None
    """
    with open(str(text_list), "w") as f:
        for element in python_list:
            f.write(str(element) + "\n")


def list_lists_to_list(list_lists, text_list):
    """
    Groups filenames from a list 'list_lists' onto a single file 'text_list'.
    Args:
        list_lists  : List containing the names of different lists
        text_list   : Name of the file onto which all the filenames from the 'list_lists' have to be appended
    Returns:
        list_name   : Python list containing the names of all the constituent files
    """
    list_name = []
    for file_name in list_lists:
        with open(str(file_name), 'r') as f:
            file_list = f.read().split()
            for elements in file_list:
                list_name.append(str(elements))
    python_list_to_text_list(list_name, str(text_list))

    return list_name

# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Functions For Manipulating 1-D Spectra (Read, Write, Smoothen etc.)
# ------------------------------------------------------------------------------------------------------------------- #
def read_1dspec(file_name):
    """
    Read 1-D Spectra from a FITS file and returns wavelength and flux arrays.
    Args:
        file_name    : FITS file from which data has to be extracted
    Returns:
        wave_array   : Array containing wavelength values extracted from the 1-D Spectra
        flux_array   : Array containing flux values extracted from the 1-D Spectra
    """
    with fits.open(str(file_name)) as hdulist:
        axis = hdulist[0].header['NAXIS']
        if axis == 1:
            flux_array = hdulist[0].data
            wave_array = spec.read_fits_spectrum1d(str(file_name)).dispersion
        else:
            flux_array = hdulist[0].data[0][0]
            wave_array = spec.read_fits_spectrum1d(str(file_name))[0].dispersion

    return wave_array, flux_array


def write_1dspec(ref_filename, flux_array, prefix_str):
    """
    Writes 1-D Spectra onto a FITS file.
    Args:
        ref_filename : FITS file from which header has to be extracted
        flux_array   : Array containing flux values
        prefix_str  : Prefix to distinguish the smoothened 1-D spectra from the original
    Returns:
        None
    """
    with fits.open(str(ref_filename)) as hdulist:
        file_header = hdulist[0].header

    output_filename = str(prefix_str) + str(ref_filename)
    remove_file(str(output_filename))
    fits.writeto(str(output_filename), data=flux_array, header=file_header)


def plot_1dspec(flux_array, wave_array):
    """
    Plots 1-D spectra.
    Args:
        flux_array   : Array containing flux values extracted from the 1-D Spectra
        wave_array   : Array containing wavelength values extracted from the 1-D Spectra
    Returns:
        None
    """
    plt.plot(wave_array, flux_array, 'g')

# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# Groups & Reads 1-D Spectra
# ------------------------------------------------------------------------------------------------------------------- #
list_fits = group_similar_files("", common_text="*_blue.0001.fits")
list_fits.sort()

for file_name in list_fits:
    wav_data, flux_data = read_1dspec(str(file_name))
    plot_1dspec(wave_array=wav_data, flux_array=flux_data)
plt.show()
# ------------------------------------------------------------------------------------------------------------------- #
