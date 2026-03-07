
## String Data Type

# It is represented by str class.
# Strings in Python can be created using single quotes, double quotes or even triple quotes.
# We can access individual characters of a String using index.

print('Hello')
print("It's alright")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

s = 'Welcome to the course'
print(s)
print(type(s))

# access string with index
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-2])   # reverse string

a = "Hello, World!"
print(len(a))

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])

# Negative Indexing
print(b[-1])
print(b[-5:-2])
print(b[-2:-5]) # wrong
print(b[-1:])

# Modify Strings

a = " Hello, World!"
print(a.upper()) # Upper Case
print(a.lower()) # Lower Case

a = " Hello, World! "
print(a.strip()) # Remove Whitespace returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Basic Operation
text = 'HI mY NAmE iS SomTHinG'
print(text.upper()) 
print(text.lower()) 
print(text.title()) 
print(text.swapcase()) 
print(text.capitalize()) 

text = "Hello, World!"
print(text.split(", ")) # Output: ['Hello', 'World!']
words = ['Hello', 'World!']
print(" ".join(words)) # Output: Hello World!

text = " Hello, World! "
print(text.strip()) # Output: Hello, World!
print(text.count("o")) # Output: 2
print("Hello".isalpha()) # Output: True
print("12345".isdigit()) # Output: True
print("hello".islower()) # Output: True
print("HELLO".isupper()) # Output: True

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# age = 36
# txt = "My name is John, I am " + age
# print(txt) #This will produce an error:

age = 36
txt = "My name is John, I am " +str(age)
print(txt)

s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)

# We can repeat a string multiple times using * operator.
s = "Hello "
print(s * 3)

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Using format()
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

# Escape Character
# txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \t	Tab	
	


# String Methods
# capitalize()	Converts the first character to upper case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# find()	Searches the string for a specified value and returns the position of where it was found
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# replace()	Returns a string where a specified value is replaced with a specified value
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# upper()	Converts a string into upper case
