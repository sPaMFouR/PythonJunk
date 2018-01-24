# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxx-----------------------------------Day 1-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# with open('test_1', 'r') as f:
# 	f.readline().rstrip()
# 	f.readline().rstrip()
# 	print f.readline().rstrip()


# print 5,
# print 6
#
# print 5
# print 6
#
# with open('align.coo', 'r') as f:
#     f.readline().rstrip()
#     f.readline().rstrip()
#     print f.readline().rstrip()

sum_total = 5


def square_add1(list_num):
    global sum_total
    for num in list_num:
        sum_total += int(num) ** 2
    return int(sum_total)


def square_add2(list_num):
    sum_total = 0
    for num in list_num:
        sum_total += int(num) ** 2
    return int(sum_total)

#
# def square_add3(list_num):
#     for num in list_num:
#         sum_total += int(num) ** 2
#     return int(sum_total)
#
# print square_add2(['3', '4'])  # prints 25
# print sum_total  # prints 5
# print square_add1(['3', '4'])  # prints 30
# print sum_total  # prints 30
# print square_add3(['3', '4'])  # Gives ERROR


def test_run():
    x = []
    y = []
    for i in range(0, 2):
        for j in range(0, 2):
            y.append(j+1)
        x.append(y)
    return x


# 1st iteration - [0, 1]
# 2nd iteration - [0, 1, 1, 2]
# final_output - [[0, 1, 1, 2], [0, 1, 1, 2]]

def test_run1():
    x = []
    for i in range(0, 2):
        y = []
        for j in range(0, 2):
            y.append(j+i)
        x.append(y)
    return x

# 1st iteration - [0, 1]
# 2nd iteration - [1, 2]
# final_output - [[0, 1], [1, 2]]

# x = raw_input("Enter The Value:")
# print x

# Reading-Writing Files
# Defining Functions
# Global and Local variables
# Example of Multiple Iterations
# Terminal Input


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxx-----------------------------------Day 2-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

import os
import glob
import re
import pyfits

# print glob.glob('*brajesh*') + glob.glob('*align*')

# random_text = 'c,v,t'
# random_list = random_text.split(',')
# print random_list


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

# print group_similar_files('list_xy', 'xy*', exceptions='')
# print group_similar_files('list_xy', 'xy*', exceptions='gr7')
# print group_similar_files('list_xy', 'xy*', exceptions='gr7,gr8')
# print group_similar_files('list_xy', 'xy*', exceptions='i,u')


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


# text_list_to_python_list('faale')


# sample_fits = raw_input("Enter the filename: ")
# sample_fits = 'brajesh_b1.fits'
# sample_header = pyfits.getheader(sample_fits)
# print sample_header.keys()
# print sample_header['OBJECT']

# list_files = group_similar_files('list_ASASSN14dq', '*ASASSN14dq*', exceptions='')
# list_RA = []
# list_DEC = []
# for file_name in list_files:
#     # fits_header = pyfits.getheader(file_name)
#     # print fits_header
#     list_RA.append(pyfits.getheader(file_name)['RA'])
#     list_DEC.append(pyfits.getheader(file_name)['DEC'])
#
# with open('log_RA_DEC', 'w') as f:
#     for kachra in range(0, len(list_RA)):
#         f.write(list_RA[kachra] + ' ' + list_DEC[kachra] + '\n')
#

# from astropy.io import fits
#
# hdulist = fits.open('ASASSN14dq-b1.fits')
# array = hdulist[0].data
# print (array)
#

#
# import astroscrappy
#
#
# def cosmic_scrappy(input_file, clip_section):
#     """
#         Corrects for cosmic rays in the OBJECT image after clipping based on the string 'clip_section'
#         Args:
#             input_file    : Name of the FITS file to be corrected for Cosmic rays
#             clip_section  : Python list containing the section of the FITS file to be copied
#         Returns:
#             None
#         """
#     iraf.imcopy(input=str(input_file) + str(clip_section), output=str(input_file), verbose='no')
#     input_array, input_header = cosmics.fromfits(str(input_file))
#
#     output_mask, output_array = detect_cosmics(input_array, gain=float(ccd_gain), readnoise=float(read_noise),
#                                                sigclip=15.0, sigfrac=0.5, satlevel=55000, cleantype='median',
#                                                verbose=True)
#
#     cosmics.tofits(outfilename='d' + str(input_file), pixelarray=output_array, hdr=input_header)
#
#
# def lacos_spec(input_file, clip_section):
#     """
#     Corrects for cosmic rays in the OBJECT image after clipping based on the string 'clip_section'
#     Args:
#         input_file    : Name of the FITS file to be corrected for Cosmic rays
#         clip_section  : Python list containing the section of the FITS file to be copied
#     Returns:
#         None
#     """
#     iraf.imcopy(input=str(input_file) + str(clip_section), output=str(input_file), verbose='no')
#
#     iraf.task(lacos_spec="/home/avinash/PyCharmProjects/Reduction_Pipeline/lacos_spec.cl")
#     iraf.lacos_spec.gain = float(ccd_gain)
#     iraf.lacos_spec.readn = float(read_noise)
#     iraf.lacos_spec.sigclip = 15.0
#     iraf.lacos_spec.sigfrac = 0.5
#     iraf.lacos_spec.objlim = 5.0
#     iraf.lacos_spec.niter = 3
#     iraf.lacos_spec.verbose = 'yes'
#
#     iraf.lacos_spec(input=str(input_file), output='d' + str(input_file))


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxx-----------------------------------Day 3-----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

random_path = '/home/avinash/'
os.chdir(random_path)


list_test = [x for x in range(0, 20, 2)]
string_test = 'bsjvdkbjlshkwlvkhel'
output_string = string_test[0:3] + string_test[3:]
output_list = list_test[0:3] + list_test[3:]
print output_list == list_test
print output_string == string_test
