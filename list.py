# List Data Type
# They are an ordered and mutable collection of items.

# Creating a List in Python
a = []

a = [1, 2, 3]
print(a)

b = ["One", "Two", "Three", 4, 5]
print(b)

# Access List Items
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# Changeable
# Allow Duplicates

list_1= ["apple", "banana", "cherry", "apple", "cherry"]
print(list_1)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Access Items
# List items are indexed and you can access them by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

print(thislist[-1:-4])

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurrence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Remove the first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
""" The clear() method empties the list.
The list still remains, but it has no content. """
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Sort List
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list descending

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Reverse Order
# The reverse() method reverses the current sorting order of the elements.
# Reverse the order of the list items
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# You can use the built-in List method copy() to copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Make a copy of a list with the ':' operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Lists
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list
# Use the extend() method to add list2 at the end of list1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

list1 = ["a", "b" , "c"]
list1.insert(3,'d')
print(list1)
""" 
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
 """

### List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Syntax
# newlist = [expression for item in iterable if condition == True]

# Normal Way 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

