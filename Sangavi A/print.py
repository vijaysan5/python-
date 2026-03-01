# The print() function prints the specified message to the screen, or other standard output device.
# The message can be a string, or any other object, the object will be converted into a string before written to the screen.

print("Hello, World!")

print("Hello", "how are you?")

x = ("apple", "banana", "cherry")
print(x)

print(1+1)

# print(a+b)

print('a'+'b')

print('1'+'1')

print('Wickipidea is a Wonderful ' + 'Website.') # we are concatenating strings inside print() function.

print("Mathurai \n is best city.") # \n to print the data to the new line.

print("Hello", "how are you?", sep="--")

# end parameter

# without end parameter
print ("Livewire is the best platform to learn Python")

# print() function ends with "**" as set in end parameter.
print ("Livewire is the best platform to Learn Python", end= "**")
print("Welcome")

# python -m asyncio ps PID or python -m asyncio pstree PID. cmd

## new updates
'''Built-ins
The bytes.fromhex() and bytearray.fromhex() methods now accept ASCII bytes and bytes-like objects. (Contributed by Daniel Pope in gh-129349.)

Add class methods float.from_number() and complex.from_number() to convert a number to float or complex type correspondingly. They raise a TypeError if the argument is not a real number. (Contributed by Serhiy Storchaka in gh-84978.)

Support underscore and comma as thousands separators in the fractional part for floating-point presentation types of the new-style string formatting (with format() or f-strings). (Contributed by Sergey B Kirpichev in gh-87790.)

The int() function no longer delegates to __trunc__(). Classes that want to support conversion to int() must implement either __int__() or __index__(). (Contributed by Mark Dickinson in gh-119743.)

The map() function now has an optional keyword-only strict flag like zip() to check that all the iterables are of equal length. (Contributed by Wannes Boeykens in gh-119793.)

The memoryview type now supports subscription, making it a generic type. (Contributed by Brian Schubert in gh-126012.)

Using NotImplemented in a boolean context will now raise a TypeError. This has raised a DeprecationWarning since Python 3.9. (Contributed by Jelle Zijlstra in gh-118767.)

Three-argument pow() now tries calling __rpow__() if necessary. Previously it was only called in two-argument pow() and the binary power operator. (Contributed by Serhiy Storchaka in gh-130104.)

super objects are now copyable and pickleable. (Contributed by Serhiy Storchaka in gh-125767.)'''
