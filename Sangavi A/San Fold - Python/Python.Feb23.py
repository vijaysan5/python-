word=["Apple", "Best", "Choco", "Enable", "Idea", "Outstanding", "Student", "Teacher", "Understanding"]
b=["A", "E", "I", "O", "U"]
Alpha=list(filter(lambda x:x[0].upper() not in (b),word))
print(Alpha)

san=[23,54,67,56,43,67,89,45,32,42,58]
even=list(filter(lambda y:y%2==0,san))
print(even)

san=[23,54,67,56,43,67,89,45,32,42,58]
even=list(map(lambda y:y%2==0,san))
print(even)
