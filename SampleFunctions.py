import copy


def add(x, y=2, z=3):
    """This is to add three numbers x, y and z. Default value of y is 2"""
    return x + y + z

print "-" * 50
print add(2, 3)
print add(10)
print add(y=1, z=5, x=2)
# print add(y=3, 5, z=6) # Incorrect, All Unnamed Variables Before The Named Variables
print "-" * 50


def list_function(list1):
    """ Arguments are passed by reference not by values"""
    list2 = list1  # A new list is not created, but the same memory location is assigned
    new_list = copy.copy(list1)  # This will create a new list
    print "List before appending:", list2
    list2.append(200)  # Changes will be reflected in the list 'list1' outside the function
    print "List after appending:", list2
    new_list.append(10000)  # Changes will NOT be reflected in the list 'list1' outside the function
    print new_list

list_outside = [2, 3, 4]
list_function(list_outside)
print list_outside  # The list is changed outside the function
print "-" * 50


sub1 = lambda c, d: c-d
print sub1(4, 2)
print "-" * 50

# Create a dictionary of functions
operation = {"add": lambda a, b: a+b,
             "subtract": lambda a, b: a-b,
             "range": lambda n: 'Within in range (0,1)' if 0 <= n <= 1 else "Not in range(0, 1)"
             }

print operation["range"](0.5)
print operation["range"](100)
print operation["add"](2, 3)
print "-" * 50

list_of_squares = [x**2 for x in range(0, 10)]
print list_of_squares
print "-" * 50

square = lambda x: x**2
print square(2)
print "-" * 50

# Using range() and lambda
list_of_squares2 = [square(x) for x in range(0, 10, 2)]
print list_of_squares2
print "-" * 50

# Using lambda on an iterator
some_list = [0, 0.5, 1, 3, 23, 100, 101, 102.5, 200]
another_list = [square(x) for x in some_list]
print another_list
print "-" * 50

# map(), filter(), reduce()
print "output of map() function"
print map(square, some_list)
print "-" * 50

print "Finding even numbers in a list using filter() function"
find_even = lambda y: y % 2 == 0
even_list = filter(find_even, some_list)
print even_list
print "-" * 50

add_list = lambda x, y: x+y
print reduce(add_list, some_list)
print "-" * 50


def add_many_numbers(x, y=3, *args, **kwargs):
    """ args is the tuple containing all the parameters which
        are passed to the function other than the default parameters

        kwargs is the dictionary containing the named parameters
    """
    try:
        a = kwargs['a']
    except Exception, e:
        print "Exception is: " + str(e)
        a = 0
    try:
        b = kwargs['b']
    except Exception, e:
        print "Exception is: " + str(e)
        b = 0

    print x, y
    print args
    print kwargs

    result = x + y
    for i in args:
            try:
                if i > 100:
                    raise "Out of range Error"
            except:
                print " Value out of range: " + str(i)
            else:
                result += i

    return result + a + b

print add_many_numbers(2,3,4,5,600,7,100, b=10000)
