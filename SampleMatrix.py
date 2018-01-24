import numpy as np


class Matrix:
    def __init__(self, rows, columns):
        self.no_of_rows = rows
        self.no_of_columns = columns
        self.matrix = np.zeros((rows, columns))

    def print_matrix(self):
        for i in range(0, self.no_of_rows):
            for j in range(0, self.no_of_columns):
                print "%d" % self.matrix[i][j],
            print "\n"

    def __add__(self, other):
        temp = np.zeros((self.no_of_rows, self.no_of_columns))
        new_matrix = np.zeros(self.no_of_rows, self.no_of_columns)
        for i in range(0, self.no_of_rows):
            for j in range(0, self.no_of_columns):
                new_matrix[i][j] = "%d" % self.matrix[i][j] + "%d" % other.matrix[i][j]
                print new_matrix[i][j]


m1 = Matrix(4, 4)
m2 = Matrix(4, 4)
m1.print_matrix()
m3 = m1+m2
print m3
