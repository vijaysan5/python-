## Errors
# Syntax Errors
# not follow the syntax rules of the language.
# detected by the interpreter or compiler at the time of parsing the code

""" 
if True
   print("This will cause a syntax error")

prnt("Hello, World!")  
print("This will cause a syntax error"
 """



## Exception Handling
# Less severe problems that occur at runtime and can be managed using exception handling 
# (e.g., invalid input, missing files).

# assert Statement
# Python evaluates the accompanying expression, which is hopefully true.
# If the expression is false, Python raises an AssertionError exception.

""" 
syntax
assert Expression[, Arguments]
 """

def KelvinToFahrenheit(Temperature): 
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32 
'''print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(1))'''
#print (KelvinToFahrenheit(0))
#print (KelvinToFahrenheit(-1))



# Try-Except Block
# used to handle exceptions and errors
# continue running even when something goes wrong.

try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print("Cannot divide by zero.")

'''try:
   numerator = int(input("Enter the numerator: "))
   denominator = int(input("Enter the denominator: "))
   result = numerator / denominator
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"Result of division: {result}")'''



# Try-Finally Block
# ensure that certain code executes, regardless of whether an exception is raised or not.
# focuses on cleanup operations that must occur, ensuring resources are properly released and critical tasks are completed.
""" 
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
 """


# Built-in Exceptions
# raise

'''def divide(a, b):
   if b == 0:
      raise ValueError("Cannot divide by zero")
   return a / b

#print(3/0)
print(divide(3,0))
try:
   result = divide(10, 0)
except ValueError as e:
   print(e)'''
