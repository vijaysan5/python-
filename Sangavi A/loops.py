### Python Loops

## while loops
# execute a set of statements as long as a condition is true.
# while (True):
#     print("Hello")

# while (False):
#     print("Hello")

i = 1
while i < 6:
  print(i) # Print i as long as i is less than 6
  i += 1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


## For Loop
# A for loop is used for iterating over a sequence

for i in range(4): # The range() function returns a sequence of numbers
    print(i)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

n = 4
for i in range(0, n):
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


### break Statement
# break statement we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(6):
  if x == 5:
     break
  print(x)

for x in range(6):
  print(x)
  if x == 5:
     break
  
### continue Statement
# continue statement we can stop the current iteration of the loop, and continue with the next
for x in range(6):
  if x == 3:
     continue
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

### pass Statement
# pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass 

for letter in 'Hello':
    pass
print('Last Letter :', letter)
