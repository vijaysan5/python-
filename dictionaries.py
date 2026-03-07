## Dictionary
# used to store data values in key:value pairs written with curly brackets.
# ordered, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("country")
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car)

thisdict["year"] = 2015

thisdict.update({"year": 2020})

print(thisdict)

thisdict.pop("country")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)
del thisdict

#print(thisdict)
#thisdict.clear()

thisdict = dict(name = "John", age = 36, country = "Norway")
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

m=thisdict.fromkeys(["brand","model"],["a","b"])

print(m["brand"])

# Dictionary Methods
""" 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary """
