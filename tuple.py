## Tuple
# items inside parentheses (), separated by commas. 
# A tuple is a collection which is ordered, unchangeable and allow duplicates.

tuple1 = (1, 5, 7, 9, 3)
tuple2 = (True, False, False)
tuple3 = ("abc", 34, True, 40, "male")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print(type(thistuple))
print(len(thistuple))                                       

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'Program')
tup3 = (tup1, tup2)
print(tup3)

tup1 = (0, 1, 2, 3)
tup2 = ("apple", "banana", "cherry")

tup3 = tup1 + tup2
print(tup3)

tup = tuple('Pneumonoultramicroscopicsilicovolcanoconiosis')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

# Creating a Tuple with repetition
tup1 = ('Programs',) * 3
print(tup1)

tup = (0, 1, 2, 3, 4)
del tup

tup = (1, 2, 3, 4, 5)
a, *b, c = tup

print(a) 
print(b) # *b collects everything in between into a list.
print(c)

tup = (1, 2, 3, [4, 5])
print(tup)

a = tuple(x for x in range(5))
print(a)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#
a=("gopinath",)*2
print(a)

a=(1,2,3)
b=("gopi","askar","mushaf")
c=a+b
print(c)

x=(1,2,3,4,5)
a,*b,c=x
print(a)
print(*b)
print(c)




a="gopi was studying datascience course in livewire"
print(a[0:30])






tup1 = (0, 1, 2, 3)
tup2 = ("apple", "banana", "cherry")

tup3 = tup1 + tup2
print(tup3)

