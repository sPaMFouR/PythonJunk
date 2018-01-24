#-*- coding: utf-8 -*-
from numpy import exp, pi

string = "HeLLo world"

print string.capitalize()
print string.title()
print string.find('o')
print string.find('heaven')
print string.replace('or', 'AND')
print string
string = string.replace('or', 'Avi')
print string

new_string = string.join("Hi fellow")
new_string2 = "".join("Hi")


string2 = "{0}+{1}={2}".format('a','b','c')
# string3 = "{0}+{1}={2}".format('a','b')

print string2
# print string3
a = 3
b = 5
print "a = {0} and b = {1}".format(a,b)

print 'Bangalore Cooordinates: {latitude}, {longitude}, Temperature = {temperature}'.format(temperature = '29ºC', latitude = '12.9667ºN', longitude = '77.5667ºE')

# C, Fortran - Compilers : .o
#              Linkers: .exe, .binary

# Python  -  Interpreter
# Line by line analysis

c = 4.56789
d = 1.2359

print 'c = {0: 5.3f}, d = {1: 4.3f}'.format(c, d)
print 'c = %f d = %d' %(c,d)

complex_number = complex(0, pi)
print "e^j*pi = {0}".format(exp(complex_number))

print "e^j*pi = {0.real: .2f} + {0.imag: .2f}".format(exp(complex_number))