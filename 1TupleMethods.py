#Tuple:
typ=("Happy", "Care", "Move", "Reach")
print(typ)
typ1=list(typ) #Change List
print(typ1)
print(type(typ1))
typ1[1]="Hundred"
typ=tuple(typ1) #Again change tuple
print(typ)
print(type(typ))

abc=(12,23,34,45,56,67,78)
x,*y,z=abc
print(x)
print(y)
print(z)

bright=(90,80,70,50)
del bright
#print(bright) = its not find. bcz this fun > del

bright=("Happy")
print(bright *2)

bright_1=tuple("Book is the best friend")
print(bright_1[:4])
print(bright_1[8:])
print(bright_1[12:-7])

Best=bright,"Future"
print(Best)

now=("List")
Best_1=(bright+"Future"+now)
print(Best_1)

new1="Beautiful"
new2="Weekend"
new_1=new1+" "+new2
print(new_1)
