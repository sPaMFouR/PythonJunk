# Object Oriented Programming


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.height = 0
        self.weight = 0
        self.fit = 'not fit'

    def print_details(self):
        print "Name: %s" % self.name
        print "Roll No: %d" % self.roll_no

    def get_name(self):
        return self.name

    def get_fitness(self, height, weight):
        self.height = int(height)
        self.weight = int(weight)

        bmi = "% 5.2f" % (float(weight) / (int(height)/100) ** 2)
        print bmi
        if 19 < float(bmi) < 24:
            self.fit = 'fit'
        return self.fit

    def __del__(self):
        print self.__class__.__name__ + " is being deleted"


student1 = Student("Avinash", 12)
student2 = Student("Prasanta", 30)

print student1.name
print student2.roll_no
print student1.print_details()

print student1.get_fitness(height=185, weight=75)


# Function Overloading
# Function adjusts to the increased number of arguments than the function originally was defined with.

# Inheritance
# Calling a Common Class From Other Classes[Vehicle - Bike, Bus, Car]

# print hasattr(student1, 'age')
# if not hasattr(student1, 'age'):
#     setattr(student1, 'age', 24)
#
# print student1.age, getattr(student1, 'age')  # Both Are Same Statements
# print student1.__dict__
# student2.test = 3
# print student2.test
#
# student_ref = student1
# print student1.name
# del student1
# del student2
# print student_ref.name
# print "Program Ends"


# Python Deletes The Objects At The End Of The Program. As The Reference Object Was Created In Between, It Deletes After
# The Execution Of The Print "Program Ends"


class Parent:
    def method1(self):
        print "Method 1 from Parent Class"

    def method2(self):
        print "Method 2 from Parent Class"


class Child(Parent):
    def method1(self):
        print "Method 1 from Child Class"

c = Child()
c.method1()
c.method2()

print isinstance(c, Child)
print isinstance(c, Parent)

