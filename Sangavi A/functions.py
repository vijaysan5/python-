## Defining a Function
# We can define a function in Python, using the def keyword.

def fun():
    print("Welcome")

fun()

def evenOdd(x): # x is a parameter
    if (x % 2 == 0): 
        return "Even"
    else:
        return "Odd"

print(evenOdd(16)) # Function Arguments
print(evenOdd(7))

def myFun(x,y): 
    print("x: ", x)
    print("y: ", y)

myFun(10,30)

def student(fname, lname):
    print(fname, lname)

student(fname='Python', lname='Practice') # Keyword Arguments
student(lname='Practice', fname='Geeks')

def nameAge(name, age): # Positional Arguments
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# Return
def my_function(x, y):
  return x + y

result = my_function(5, 3)
result2 = my_function(10,2)
print(result)
print(result2)

a,b=5,10
print(a,b)

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

x,*y=20,30,40
print(x,y)

## Arbitrary Arguments
# *args in Python (Non-Keyword Arguments):
    # the function will receive a tuple of arguments and can access the items accordingly.
# **kwargs in Python (Keyword Arguments):
    #the function will receive a dictionary of arguments and can access the items accordingly.

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)


    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='To', mid='My', last='Home')

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)

## Recursion
# Recursion is a programming technique where a function calls itself either directly.
# meaning that you can loop through data to reach a result.

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1) # function call

print(factorial(5))

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
print(tri_recursion(6))

## Lambda
# lambda keyword is used to create anonymous functions.

def cube(x):
    return x*x*x   # without lambda
print(cube(2))

cube_l = lambda x : x**3  # with lambda
print(cube_l(2))

x = lambda a, b : a * b
print(x(5, 6))

# Mapping
# applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

def square(x):
    return x * x

sq = list(map(square, numbers))
print(sq)

# filter()
# function creates a list of items for which a function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


