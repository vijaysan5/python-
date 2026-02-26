'''
a="sandhiya"
print(a[:3].lower(),end=(""))
print(a[-5:-4].upper(),end=(""))
print(a[-4:].lower())
print(a.title())
print(a.startswith("san"))
print(a.endswith("ya"))
print(a.encode())
b=a.encode()
print(b)
print(b.decode())
c="  anandh sangavi "
print(c)
print(c[-8:].title(),c[2:8].title())
a=18
b=input("age:")
print(b)
c=int(b)
print(c)
if(a==c):
    print("Age is equal")
if(a<c):
    print("a is eligible to vote")
if(a<c):
    print("a is eligible to vote")
else:
    print("a is not eligible to vote")

a=input("name:")
b=int(input("age:"))
c=input("place:")
d=18
h="Mayiladuthurai"
if(b>d and c==h):
    print("a is eligible to Vote")
if(b>d):
    print("is eligible")
else:
     print("is not eligible")
if(c==h):
    print("is accepted")
else:
    print("is not accepted")

x=input("Name:")
a=int(input("Tamil:"))
b=int(input("English:"))
c=int(input("Maths:"))
d=int(input("Hindi:"))
e=int(input("EVS:"))

if(a>35) and (b>35)and(c>35)and(d>45) and (e>25):
    print("Pass")
else:
    print("Fail")
x=input("")
'''
a=int(input("k:"))
b=""
for x in a:
    if a.