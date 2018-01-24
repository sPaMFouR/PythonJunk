import numpy as np

a = np.arange(1, 10, 2)
print a

x = list([])
x.append(2)
x.append(3)
x.append(4)
print x

x = np.array(x)
print x

x = list(x)
y = np.linspace(1, 10, 20)  # All points are spaced "(x2-x1)/(x3-1)" apart
y1 = np.logspace(0, 1, 20)

z = list([])
z.append(2)
z.append(3)
z.append(4)

z = np.array(z)
# Examples Of Broadcasting
print z + 1
print z**2

np.trim_zeros(x, 'b')
"""
b = []
b.append('4'); b.append('7'); b.append('9')
b = np.array(b)
print b + 1
"""

c = np.arange(0, 30)
d = c.reshape(5, 6)
print d[0,0]
print d[0]
print d[:, 2]
print d[:, 2:4]
print d[:, 2:]  # Equal To "print d[:, 2:6]
print d[:, 2:-2]
print d[:, ::2]  # Prints End To End With Columns Spaced By 2
print d[:, 0:-1:2]  # Prints End To End(Excluding The Last Value) With Columns Spaced By 2
print d[:, ::-1]  # End To End In Reverse

d[:, 2] = np.ones((1,5))  # The Column Is Replaced By A Column Of 'Ones'
d[:, 3] = 5  # All Elements Of The Column Are Replaced By 5
d[::2, ::2] = 100  # Replace The Value In Alternate Rows And Columns


e = d
f = d.copy()
d[:, :] = 6
print "This is d:"
print d
print "This is e:"
print e
print "This is f:"
print f
print f.flatten()

identity_matrix = np.identity(3)
print identity_matrix
identity_matrix_of_any_shape = np.eye(3, 4)
print identity_matrix_of_any_shape

g = [[2, 3, 4], [5, 6, 7]]
bigger_g = np.tile(g, (2, 3))

print g
print bigger_g
h = [x**2 for x in range(0, 10)]  # Creates A List Of Square Numbers
# Same As Above : h = [x**2 for x in np.arange(0, 10)]
print h

empty_list = [[[] for i in range(0, 10)] for j in range(0, 10)]
print empty_list
