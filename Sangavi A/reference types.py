# Iterators
# object that contains a countable number of values.

""" a='Papper'
b=iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# print(next(b)) """

""" class num:
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        a=self.n
        self.n += 1
        return a

b=num()
it=iter(b)

print(next(it))
print(next(it))
print(next(it))
print(next(it)) """

""" class num:
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<8:
            a=self.n
            self.n += 1
            return a
        else:
            raise StopIteration

b=num()
it=iter(b)

for i in it:
    print(i) """

""" li=[100, 200, 300]
it=iter(li)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break """

# Generators
# functions that can pause and resume their execution.
# Instead of using return, generators use the yield keyword.

""" def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value) """

""" def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

counter = count_up_to(5)
for number in counter:
    print(number) """

""" def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(gen) """

# send() Method
""" def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) 
gen.send("Hello")
gen.send("World") """

# close() Method
""" def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close() """

# closure

""" def functionA(name):
   name ="New name"
   def functionB():
      print (name)
   return functionB
   
myfunction = functionA("My name")
myfunction() """

""" def functionA():
   print ("Outer function")
   def functionB():
      print ("Inner function")
   functionB()

functionA() """

""" def outer_function(x):
    y = 10
    
    def inner_function(z):
        return x + y + z  
    
    return inner_function

closure = outer_function(5)
result = closure(3)
print(result)   """

# Decorator
# add extra behavior to a function, without changing the function's code.

""" def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello"

print(myfunction()) """

""" def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return f"Hello {func()} Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction()) """