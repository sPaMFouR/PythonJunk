import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.table import Table


# def time_it(file_name, points):
#     with open(file_name, 'w') as fw:
#         for index in range(0, points):
#             fw.write(str(index) + str(index + 1) + "\n")
#
#     time1 = time.time()
#
#     with open(file_name, 'r') as fr:
#         data1 = fr.read().split()
#
#     time2 = time.time()
#
#     with open(file_name, 'r') as fr:
#         data2 = []
#         for line in fr:
#             data2 += line.split()
#
#     time3 = time.time()
#
#     df = pd.read_csv(file_name, skiprows=1)
#     data_3 = df[:]
#
#     time4 = time.time()
#
#     return time2-time1, time3-time2, time4-time3
#
# file1 = 'Test_data.dat'
# list_points = np.arange(10000, 1000001, 10000)
# with open(file1, 'w') as fw:
#     for index in range(0, 100000):
#         fw.write(str(index) + "\n")
# list_time = np.array([time_it(file1, point) for point in list_points])
#
# plt.semilogy(list_points, list_time[:, 0], label="Open & Read")
# plt.semilogy(list_points, list_time[:, 1], label="Open & Readlines")
# plt.semilogy(list_points, list_time[:, 2], label="ReadCSV Pandas")
# # plt.semilogy(list_nums, list_time[:, 3], label="Numpy Zeros + Equate")
# plt.grid()
# plt.legend()
# plt.show()


def time_it(file_name, points):
    with open(file_name, 'w') as fw:
        for index in range(0, points):
            fw.write(str(index) + str(index + 1) + "\n")
    time1 = time.time()

    with open(file_name, 'r') as fr:
        data_line = fr.readline().split()
        data1 = fr.read().split()
        data1 = data_line + data1

    col1 = len(data_line)
    row1 = int(len(data1) / col1)
    data1_col1 = [[data1[j + i * col1] for j in range(0, col1)] for i in range(0, row1)]

    time2 = time.time()

    with open(file_name, 'r') as fr:
        data2 = []
        for line in fr:
            data2 += line

    col2 = len(data2[0].split())
    row2 = len(data2)
    data1_col2 = [line.split() for line in data2]

    time3 = time.time()

    df = pd.read_csv(file_name, skiprows=1)

    time4 = time.time()

    f0 = np.loadtxt(file_name, dtype=int)

    time5 = time.time()

    f1 = np.loadtxt(file_name)

    time6 = time.time()

    f2 = Table.read(file_name, format='ascii',)

    time7 = time.time()

    return time2-time1, time3-time2, time4-time3, time5-time4, time6-time5, time7-time6

file1 = 'Test_data.dat'
# list_points = np.arange(1000, 20001, 1000)
# list_time = np.array([time_it(file1, point) for point in list_points])
#
# plt.semilogy(list_points, list_time[:, 0], label="Open & Read")
# plt.semilogy(list_points, list_time[:, 1], label="Open & Readlines")
# plt.semilogy(list_points, list_time[:, 2], label="ReadCSV Pandas")
# plt.semilogy(list_points, list_time[:, 3], label="Numpy (Mentioned Datatype)")
# plt.semilogy(list_points, list_time[:, 4], label="Numpy (Without Mentioning Datatype)")
# plt.semilogy(list_points, list_time[:, 5], label="Astropy Tables")
#
# plt.grid()
# plt.legend()
# plt.show()

with open(file1, 'w') as fw:
    for index in range(0, 1000000):
        fw.write(str(index) + str(index + 1) + "\n")


def _make_gen(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)


def rawgencount(filename):
    f = open(filename, 'rb')
    f_gen = _make_gen(f.read)
    return sum(buf.count(b'\n') for buf in f_gen)

time1 = time.time()

print rawgencount(file1)

print time.time() - time1
