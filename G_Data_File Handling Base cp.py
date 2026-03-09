### File Handling
""" 
file = open("filename", "mode") """

""" 
Modes
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images) 

"+" - open file for updating (reading and writing)

"rb" - Opens a file for reading only in binary format. This is the default mode.

"r+" - Opens a file for both reading and writing.

"rb+" - Opens a file for both reading and writing in binary format.
"""

"""
# Opening a file in read mode
 file = open("sample.txt", "r")

# Opening a file in write mode
file = open("sample.txt", "w")

# Opening a file in append mode
file = open("sample.txt", "a")

# Opening a file in binary read mode
file = open("sample.txt", "rb")

fo = open("sample.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close() """



# write
""" 
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content """

""" file = open("sample.txt", "w")
file.write("Hello")
file.close()
print ("File opened successfully!!")  """


""" with open("sample.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content added Successfully!!")  """

# with open("sample.txt", "a") as f:
#   f.write("Now the file has more content!")



# Reading a File
""" 
read() − Reads the entire file.

readline() − Reads one line at a time.

readlines − Reads all lines into a list. """

""" file= open("sample.txt", "r")
content = file.read()
print(content) """

# with open("sample.txt", "r") as f:
#  print(f.read()) 


# with open("sample.txt", "r") as file:
#    line = file.readline()
#    print(line)
#    print(file.readline()) 


# with open("sample.txt", "r") as file:
#    lines = file.readlines()
#    print(lines) 

# file = open("sample2.txt",'x')
# print("file created")


# Binary Mode Read & Write
""" with open('sample.txt', 'wb') as f:
   # Binary data
   data = b"Hello World"  
   f.write(data) 

 with open('sample.txt', 'wb') as f:
   # Convert text string to bytes
   data = "Hello World".encode()  
   f.write(data)

with open('sample.txt', 'wb') as f:
   f.write(data) 


 with open('sample.txt', 'rb') as f:
   data = f.read()
   print(data.decode())"""



# Reading and Writing Modes

# seek() Method
# used to set the position of the read/write pointer within the file.

""" fo=open("sample.txt", "w+")
# Write initial data to the file
fo.write("This is a rat race")

# Move the read/write pointer to the 10th byte
fo.seek(10, 0)

# Read 3 bytes from the current position
data = fo.read(3)
print(data)
# Move the read/write pointer back to the 10th byte
fo.seek(10, 0)

# Overwrite the existing content with new text
fo.write('cat')

# Close the file
fo.close() """

# r+" Mode
# read and write
 with open("sample.txt", "r+") as fo:

   fo.write("This is a rat race")

   # Rewind the pointer to the beginning of the file
   fo.seek(0)
   data = fo.read()
   print(data)

with open("sample.txt", "r+") as fo:
   # Move the read/write pointer to the 10th byte position
   fo.seek(10, 0)
   data = fo.read(3)
    
   print(data) 


 fo = open("sample.txt", "w+")

fo.write("This is a rat race")

fo.seek(10, 0)
data = fo.read()
print("Data read from position 10:", data)

data = fo.read(3)
print("Data read from position 10:", data)

fo.seek(10, 0)
fo.write("cat")

fo.seek(0, 0)
data = fo.read()
print("Updated file content:", data)

fo.close()


## Create a New File
# "x"  − Opens the file for exclusive creation. already exists, the operation fails.

# f = open("myfile.txt", "x")

n=open("myfile.txt", "r+")

n.write("This is newly created")  

n.seek(0)
r=n.read()
print(r) 


## Delete File
# To delete a file, you must import the OS module, and run its os.remove() function.

import os
os.remove("test.bin")

import os
if os.path.exists("test.bin"):
  os.remove("test.bin")
else:
  print("The file does not exist")

# Delete Folder
# use the os.rmdir() method:
import os
os.rmdir("myfolder")


### Handling Exceptions
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except:
    print("There is no such file")
finally:
    print("Program successfully execited") """
