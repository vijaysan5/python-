# Python Operators
# Operators are used to perform operations on variables and values.

## Types
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

## Arithmetic Operators
# Variables
a = 2
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b) # Not consider point value 

# Modulus
print("Modulus:", a % b) # Return division balance

# Exponentiation
print("Exponentiation:", a ** b) # Power Value

## Comparison Operators
# compares values. It either returns True or False according to the condition.

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

## Logical Operators
# It is used to combine conditional statements.

a = True
b = False
print(a and b)
print(a or b)
print(not a)

## Bitwise Operators
# act on bits and perform bit-by-bit operations.
# These are used to operate on binary numbers.

# Bitwise Operators in Python are as follows

# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR

a = 4 # 100
b = 2 # 010

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

## Assignment Operators
# used to assign values to the variables
# value of the right side of the expression to the left side operand.

b = 10
print(b)
b += 3
print(b)
b -= 1
print(b)
b *= 2
print(b)
b=5
b <<= 1 # moving binary of  b to the a times return acctual value.
print(b)

## Identity Operators
# is and is not are the identity operators both are used to check if two values are located on the same part of the memory.
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

## Membership Operators
# in and not in are the membership operators that are used to test whether a value or variable is in a sequence.
x = 24
y = 20
lis = [10, 20, 30, 40, 50]

print(x not in lis)
print(y in lis)

a="hello"
print("e" in a)
