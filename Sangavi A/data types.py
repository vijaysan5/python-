### Data Types

# Numeric: int, float, complex
# Sequence Type: string, list, tuple, Set
# Mapping Type: dict
# Boolean: bool

## Numeric Data Types
# int
a = 5 
print(type(a))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float
b = 5.0 
print(type(b))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

z = -87.7e100
print(type(z))

# Complex 
# only j imaginary part
c = 2 + 4j 
print(type(c))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

## Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods.

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

z = int("3") # # z will be 3

z = float(3)   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str(1) # x will be '1'


### Sequence Data Types
# String Data Type
s = 'Welcome'
print(s)
print(type(s))

a = "Welcome"
print(a)

c = """Hi,
Good to 
see you!"""
print(c)

b = '264'
print(type(b))

# access string with index
print(s[1])
print(s[2])
print(s[-1])


# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers

name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# 2 desimals
number = 3.14159
rounded_number = round(number, 2)
print(rounded_number)

number = 3.14159
formatted_string = f"{number:.2f}"
print(formatted_string)

number = 3.14159
formatted_string = "{:.2f}".format(number)
print(formatted_string)

number = 3.14159
formatted_string = "%.2f" % number
print(formatted_string)

# List Data Type
# inside the square brackets[].
# List items are ordered, changeable, and allow duplicate values.
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["One", "Two", "Three", 4, 5]
print(b)

# Access List Items
a = ["One", "Two", "Three"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

print(a[0:1])
print(a[1:])
print(a[-1:])

# Tuple Data Type
# Creating a Tuple in Python
# A tuple is a collection which is ordered and unchangeable allow duplicate
# initiate empty tuple
tup1 = ()

tup2 = ('Hello', 'World')
print("\nTuple with the use of String: ", tup2)

t=(1,2,3)
t2=t+(4,)
print(t2)

# Access Tuple Items
tup1 = tuple([1, 2, 3, 4, 5])
# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])



##Boolean Data Type 
# Python Boolean Data type is one of the two built-in values
# True or False.
a = True
b = False
c = True
print(type(a))
print(type(b))
print(type(c))

## Set Data Type
# Create a Set
# Sets can be created by using the built-in set() function.
# an iterable object or a sequence by placing the sequence inside curly braces{}
# A set is a collection which is unordered, unchangeable, and unindexed.
# initializing empty set
s1 = {}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# Dictionary Data Type
# A Dictionary holds a key: value pair
# Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Create a Dictionary
# initialize empty dictionary
d = {}

d = {1: 'Red', 2: 'Green', 3: 'Blue'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Red', 2: 'Green', 3: 'Blue'})
print(d1)

# Accessing Key-value
d = {1: 'Good', 'name': 'Well', 3: 'Done'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))

print(d.keys())
print(d.values())
print(d.items())

## Arrays
# Arrays are used to store multiple values in one single variable:
# arrays in Python you will have to import a library

cars = ["Ford", "Volvo", "BMW"]
print(cars)

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

x = len(cars)
print(x)

cars.append("Honda")
print(cars)

cars.pop() # remove last element
print(cars)

cars.pop(1) # remove 2 element
print(cars)

cars.remove("Volvo") # Delete the element that has the value "Volvo"
print(cars)

"""Array Methods
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list"""
