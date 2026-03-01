#syntax
"""
if True:
    works
"""

### If Conditional Statement
# It executes a block of code if the given condition is true.
""" 
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops. """

age = 20
if age >= 18:
    print("Eligible to vote.")

a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


## Elif
# if the previous conditions were not true, then try this condition

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

## Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

## Nested If
# if statements inside if statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
