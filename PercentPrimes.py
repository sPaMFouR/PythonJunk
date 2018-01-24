#!/usr/bin/env python
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxx-------------------CALCULATION OF PRIME NUMBERS-----------------xxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

# ------------------------------------------------------------------------------------------------------------------- #

import math
import time
# from blist import blist
import numpy as np

# ------------------------------------------------------------------------------------------------------------------- #


class FastArray:

    def __init__(self, largest_no, array_primes):
        self.data = array_primes
        self.capacity = largest_no
        self.size = len(array_primes)
        self.current_index = 0

    def update(self, x):
        self.size += 1
        newdata = np.zeros((self.size,))
        newdata[:self.size-1] = self.data[:self.size]
        self.data = newdata
        self.data[self.size-1] = x

        return self.data

    def update2(self, x):
        newdata = np.zeros((self.capacity,))
        newdata[:self.size] = self.data[:self.size]
        self.data = newdata
        self.data[self.size] = x
        self.size += 1

        return self.data

    def update3(self, x):
        self.data[self.current_index] = x
        self.current_index += 1

        return self.data


# list_num = np.array([2, 3])
# list_num3 = np.zeros((100, ))
# object_num = FastArray(5, list_num)
# object_num3 = FastArray(100, list_num3)
# list_num = object_num.update(1)
# print list_num
# list_num = object_num.update(2)
# print list_num
# list_num3 = object_num3.update3(1)
# print list_num3
# list_num3 = object_num3.update3(2)
# print list_num3
# list_num3 = object_num3.update3(5)
# print list_num3
# ------------------------------------------------------------------------------------------------------------------- #

def calculate_prime_percent(user_input_number):
    largest_no = int(user_input_number)
    list_primes = []
    list_numbers = [number for number in range(1, largest_no + 1)]

    for number in list_numbers:
        if number / 2. < 1:
            continue
        elif number / 2. == 1:
            list_primes.append(number)
        if number / 2 > 1:
            closest_sqrt = math.ceil(math.sqrt(number))
            list_divisors = [divisor for divisor in list_primes if divisor <= closest_sqrt]
            factor_count = 0
            for primes in list_divisors:
                if number % primes == 0:
                    factor_count += 1
                    break
            if factor_count == 0:
                list_primes.append(number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))

    return percent_primes


def calculate_prime_percent2(user_input_number):
    largest_no = int(user_input_number)
    list_primes = []
    list_numbers = [number for number in range(1, largest_no + 1)]

    for number in list_numbers:
        if number / 2. < 1:
            continue
        elif number / 2. == 1:
            list_primes.append(number)
        else:
            closest_sqrt = math.ceil(math.sqrt(number))
            # list_divisors = [divisor for divisor in list_primes if divisor <= closest_sqrt]
            factor_count = 0
            for primes in list_primes:
                if primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
            if factor_count == 0:
                list_primes.append(number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))

    return percent_primes


def calculate_prime_percent3(largest_no):
    list_primes = np.empty(shape=(0, 0), dtype=int)
    list_numbers = np.arange(1, int(largest_no))[::2]

    for number in list_numbers:
        if number / 2. < 1:
            continue
        elif number / 2. == 1:
            list_primes = np.append(list_primes, number)
        else:
            closest_sqrt = int(number ** 0.5) + 1
            factor_count = 0
            for primes in list_primes:
                if primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
            if factor_count == 0:
                list_primes = np.append(list_primes, number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))

    return percent_primes


def calculate_prime_percent4(largest_no):
    list_primes = [2, 3]
    list_numbers = [number for number in range(5, largest_no + 1, 2) if number % 6 == 1 or number % 6 == 5 or
                    number % 5 != 0]

    for number in list_numbers:
        # if number / 2 == 1:
        #     list_primes.append(number)
        # else:
        closest_sqrt = int(number ** 0.5) + 1
        factor_count = 0
        for primes in list_primes:
            if primes < closest_sqrt:
                if number % primes == 0:
                    factor_count += 1
                    break
        if factor_count == 0:
            list_primes.append(number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def calculate_prime_percent5(largest_no):
    list_primes = []
    list_numbers = [number for number in range(2, largest_no + 1)]

    for number in list_numbers:
        if number / 2 == 1:
            list_primes.append(number)
        else:
            closest_sqrt = int(number ** 0.5) + 1
            factor_count = 0
            for primes in list_primes:
                if primes <= closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
            if factor_count == 0:
                list_primes.append(number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def calculate_prime_percent6(largest_no):
    list_primes = [2, 3]
    list_numbers = [number for number in range(5, largest_no + 1, 2) if number % 3 != 0]
    list_divisors = []
    print list_numbers
    for number in list_numbers:
        closest_sqrt = int(number ** 0.5) + 1
        factor_count = 0
        if len(list_divisors) != 0:
            for primes in list_divisors:
                if primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
        if factor_count == 0:
            list_divisors.append(number)

    list_primes = list_primes + list_divisors
    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def calculate_prime_percent7(largest_no):
    list_numbers = [number for number in range(5, largest_no + 1) if number % 6 == 1 or number % 6 == 5]
    list_primes = np.array([2, 3])
    list_divisors = np.array([])
    object_primes = FastArray(int(largest_no), list_divisors)

    for number in list_numbers:
        closest_sqrt = int(number ** 0.5) + 1
        factor_count = 0
        if len(list_divisors) != 0:
            for primes in list_divisors:
                if primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
        if factor_count == 0:
            list_divisors = object_primes.update(number)

    list_primes = np.append(list_primes, list_divisors)
    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def calculate_prime_percent8(largest_no):
    list_numbers = [number for number in range(5, largest_no + 1) if number % 6 == 1 or number % 6 == 5]
    list_primes = np.array([2, 3])
    list_divisors = np.zeros((largest_no,))
    object_primes = FastArray(int(largest_no), list_divisors)

    for number in list_numbers:
        closest_sqrt = int(number ** 0.5) + 1
        factor_count = 0
        if len(list_divisors) != 0:
            for primes in list_divisors:
                if 3 < primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
        if factor_count == 0:
            list_divisors = object_primes.update3(number)

    list_primes = np.append(list_primes, np.trim_zeros(list_divisors, 'b'))
    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def calculate_prime_percent9(largest_no):
    list_primes = [2, 3]
    list_numbers = [number for number in range(5, largest_no + 1) if number % 6 == 1 or number % 6 == 5]
    list_divisors = blist([])

    for number in list_numbers:
        closest_sqrt = int(number ** 0.5) + 1
        factor_count = 0
        if len(list_divisors) != 0:
            for primes in list_divisors:
                if primes < closest_sqrt:
                    if number % primes == 0:
                        factor_count += 1
                        break
        if factor_count == 0:
            list_divisors.append(number)

    list_primes += list(list_divisors)
    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


def exp_by_squaring(num, exp):
    if exp < 0:
        return exp_by_squaring(1 / num, -exp)
    elif exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0:
        return exp_by_squaring(num * num, exp / 2)
    elif exp % 2 == 1:
        return exp_by_squaring(num * num, (exp - 1) / 2)


def exp_by_squaring2(num, exp):
    if exp % 2 == 0:
        return exp_by_squaring(num * num, exp / 2)
    elif exp % 2 == 1:
        return exp_by_squaring(num * num, (exp - 1) / 2)


def calculate_prime_percent10(largest_no):
    list_primes = [2, 3]
    list_numbers = [number for number in range(5, largest_no + 1) if number % 6 == 1 or number % 6 == 5]

    for number in list_numbers:
        factor_count = 0
        for primes in list_primes:
            if exp_by_squaring2(primes, number - 1) / number != 1:
                factor_count += 1
                break
        if factor_count == 0:
            list_primes.append(number)

    percent_primes = ((len(list_primes) * 100) / float(largest_no))
    return percent_primes


# ------------------------------------------------------------------------------------------------------------------- #

list_num = [index for index in range(10000, 100001, 10000)]
list_time_taken = []
list_time_taken2 = []

print "Numbers:     Process-4       Process-6"
for num in list_num:
    start_time = time.time()
    percent_prime = calculate_prime_percent4(int(num))
    time_taken = time.time() - start_time
    start_time2 = time.time()
    percent_prime2 = calculate_prime_percent6(int(num))
    time_taken2 = time.time() - start_time2
    # start_time3 = time.time()
    # percent_prime3 = calculate_prime_percent3(int(num))
    # time_taken3 = time.time() - start_time3
    print "{0:8f} {1:>9.4f} {2:>9.4f}".format(num, time_taken, time_taken2),
    print "{0:>6.3f} {1:>6.3f}".format(percent_prime, percent_prime2)
# ------------------------------------------------------------------------------------------------------------------- #
