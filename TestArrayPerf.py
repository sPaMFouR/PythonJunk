# import os
# from astropy.table import Table
#
# TEST_DIR = "/home/avinash/Test/Avinash/"
# os.chdir(TEST_DIR)
#
# file_name = 'stars.coo'
# file_name1 = 'afbs_ASASSN14dq-v1.fits'
# file_name2 = 'output_instr_nov17'
# file_name3 = 'test.mag.4'
# table1 = Table.read(file_name3, format='ascii.daophot')
#
# print table1.keys()
# table1.keep_columns(["ID", "IMAGE", "IFILTER", "XCENTER", "YCENTER", "MSKY", "XAIRMASS", "RAPERT1", "MAG1", "MERR1"])
#
# table1.write('table1.dat', format='ascii.ecsv', overwrite=True)

import time
import numpy as np
import matplotlib.pyplot as plt

list_nums = range(0, 100000, 1000)


def time_it(num):
    time1 = time.time()

    list_1 = []
    for i in range(0, num):
        list_1.append(i)

    time2 = time.time()

    list_2 = [i for i in range(0, num)]

    time3 = time.time()

    list_3 = np.arange(0, num)

    time4 = time.time()

    list_4 = np.zeros(num)
    for i in range(0, num):
        list_4[i] = num

    time5 = time.time()

    list_5 = np.array([])
    for i in range(0, num):
        list_5 = np.append(list_5, num)

    time6 = time.time()

    return time2-time1, time3-time2, time4-time3, time5-time4, time6 - time5

list_time = np.array([time_it(num) for num in list_nums])

plt.semilogy(list_nums, list_time[:, 0], label="List Append")
plt.semilogy(list_nums, list_time[:, 1], label="List Comprehensions")
plt.semilogy(list_nums, list_time[:, 2], label="Numpy Arange")
plt.semilogy(list_nums, list_time[:, 3], label="Numpy Zeros + Equate")
plt.semilogy(list_nums, list_time[:, 4], label="Numpy Append")
plt.grid()
plt.legend()
plt.show()


# list_nums = range(0, 10000000, 10000)
#
# def time_it(num):
#     time1 = time.time()
#     list_3 = np.linspace(0, num, num)
#     time2 = time.time()
#     return time2-time1
#
# list_time = [time_it(num) for num in list_nums]
# plt.semilogy(list_nums, list_time, label="List Append")
# plt.grid()
# plt.show()

