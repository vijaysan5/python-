'''words=['Healthy', 'Family', 'Ability', 'Idinty', 'Cut', 'Out']
b=['A', 'E', 'I', 'O', 'U']
for x in words:
    if x[0] not in b:
        print(x)

word=['Healthy', 'Family', 'Ability', 'Idinty', 'Cut', 'Out']
for a in word:
    if "u" in a:
        print(a)
'''
       
#set
frts={"Apple", "Blueberry", "Strawberry", "Pineapple"}
print(frts)

colour={"Pink", "Blue", "Red"}
print(colour)
frts.update(colour)
print(frts)

best={"Kiwi", "Gova"}
best.update(frts)
print(best)

newone={"Blue", "pink", "Green"}
newother={"Berry", "Cherry"}
newone.update(newother)
print(newone)

newother.remove("Cherry")
print(newother)
newone.discard("Green")
print(newone)
print("________________________________________")
print(frts)
abc=frts.pop()
print(abc)
print(frts)

colour.clear()
print(colour)

cv_1={"ab", "ac", "ad", "af"}
cv_2={1, 2, 5, 7, 9}
cv_3=cv_1.union(cv_2)
print(cv_3)

ab={"ab", "af",}
ac={"Blue", "pink"}
ad={1,3,5}
abcd=ab | ac | ad
print(abcd)
ab.update(ac)
print(ab)

#intersection
mn1={"Blueberry", "Cherry", "Strawberry"}
mn2={"Berry", "Cherry", "Pineapple"}

mx1=mn1.intersection(mn2)
mx2=mn1 & mn2
print(mx1)
print(mx2)

mn1.intersection_update(mn2) #update
print(mn1)

#difference
ab1={"Blueberry", "Cherry", "Strawberry"}
ab2={"Berry", "Cherry", "Pineapple"}
ab3= ab1.difference(ab2)
ab4=ab1^ab2
print(ab3)
print(ab4)


#frozenset
words=frozenset({'Healthy', 'Family', 'Ability', 'Idinty', 'Carry'})
print(words)

