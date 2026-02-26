#change
clrs=["Red", "Blue", "Green", "Yellow"]
clrs[2]="Babypink"
print(clrs)

clrs=["Red", "Blue","Babypink", "Green", "Yellow"]
clrs[1:3]="Indigo", "Lavender"
print(clrs)
#Insert
clrs=["Red", "Blue","Babypink", "Green", "Yellow"]
clrs.insert(3,"Pistagreen")
print(clrs)
#Add
clrs=["Red", "Blue","Babypink", "Green", "Yellow"]
clrs.append("Rose")
print(clrs)
#Extend
clrs=["Red", "Blue","Babypink", "Green", "Yellow"]
clrs123=["Rose", "Silver"]
clrs.extend(clrs123)
print(clrs)
#Add any
clrs=["Red", "Blue","Babypink", "Green", "Yellow"]
colour=("Gold")
clrs.extend(colour)
print(clrs)
#Remove
clrs=["Babypink", "Red", "Blue","Babypink", "Green", "Silver", "Yellow"]
clrs.remove("Babypink")
print(clrs)
#pop(),(dig)
fruits=["Mango", "Blueberry", "Apple", "Orange"]
fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)
clrs=["Babypink", "Red", "Blue", "Babypink", "Green", "Silver", "Yellow"]
del clrs[0]
print(clrs)
#Delete
fruits=["Mango", "Blueberry", "Apple", "Orange", "Dragonfruit"]
del fruits
#Clear
fruits=["Mango", "Blueberry", "Apple", "Orange"]
fruits.clear()
print(fruits)
#Sort
Colour=["Blue", "Silver", "Gold", "Pistagreen", "Green", "While"]
Colour.sort()
print(Colour)
#sort with reverse=True
Colour=["While", "Blue", "Silver", "Gold", "Pistagreen", "Green"]
Colour.sort(reverse=True)
print(Colour)
Digits=[45,65,84,23,65,99]
Digits.sort(reverse=True)
print(Digits)
#reverse()
Colour=["While", "Blue", "Silver", "Gold", "Pistagreen", "Green"]
Colour.reverse()
print(Colour)
#copy()
fruits5=["Mango", "Blueberry", "Apple", "Orange", "Kiwi", "Cherry"]
self=fruits5.copy()
print(self)
fruitname=["Mango", "Apple"]
self_1=list(fruitname)
print(self_1)
#Join
Colour=["While", "Blue", "Silver"]
FruitNM=["Mango", "Apple"]
CF=Colour+FruitNM
print(CF)

san=["AB", "AC", "AD", "AE"]
for a in san:
    abcdjoin=a
    print(abcdjoin)
san.insert(5, "AG")
print(san)
    

