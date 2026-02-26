def an(m):
    return m*m*m
print(an(2))

I=lambda n:n**3
print(I(2))

II=lambda a,b:a*b
print(II(21,5))

Inum=[2,4,9,7,8]
mvalue=list(map(lambda a:a*3,Inum))
print(mvalue)

IInum=[23,89,80,58,45,34]
addvalue=list(map(lambda b:b+2,IInum))
print(addvalue)

IIInum=[45,48,34,89,76]
Sample1=list(filter(lambda c:c%2==0,IIInum))
print(Sample1)
Sample2=list(filter(lambda d:d%2!=0,IIInum))
print(Sample2)
'''
IVnum=[86,78,56,45,35,23,21]
mapfil=list(map(lambda e:e%2==0,IVnum))
print(mapfil)
mapfil2=list(map(lambda f:f%2!=0,IVnum))
print(mapfil2)
alpha=["Home", "Our Family", "Anniversary", "Everythin", "My Family", "Teacher"]
    alf=list(filter(lambda x:x=="A" and "E"
    print(x)
'''
a=["Home", "Our Family", "Anniversary","Teacher", "Earth", "Birthday"]
b=["a", "e", "i", "o", "u"]
al=list(filter(lambda xy:xy[0].lower() not in (b),a))
print(al)






