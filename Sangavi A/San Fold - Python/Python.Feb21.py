'''a=56
b=89
c=58
v=30
def use():
    if(a<v) and (b<v) and (c<v):
        print("HDFC")
    else:
        print("fjhug")
use()


xy=35
Tam=int(input("Tam:"))
Eng=int(input("Eng:"))
EVS=int(input("evs:"))
Hindi=int(input("Hn:"))
def answer():
    if (xy<Tam) and (xy<Eng) and (xy<EVS) and (xy<Hindi):
        print( "Pass" )
    else:
        print( "Fail" )
answer()
'''
def sanvi(en,an,yn):
    print("Name:",en)
    print("Place:",an)
    print("Pincode:",yn)
sanvi("vijay", "Mayiladuthurai", "609001")

def leo(n):
    return n*n*n
print(leo(3))

jleo=lambda m:m**2
print(jleo(5))

hnum=lambda k,v:k+v
print(hnum(21,23))

jnm=[2,4,3,6,5,8]
knm=list(map(lambda x:x*5,jnm))
print(knm)

abc=[23,89,54,14,3,24,68,90]
Even=list(filter(lambda a:a%2==0,abc))
print(Even)

efg=[23,89,54,14,3,24,68,90]
Odd=list(filter(lambda x:x%2!=0,efg))
print(Odd)

start=[23,89,54,14,3,24,68,90]
end=list(map(lambda a:a%2==0,start))
print(end)

start1=[23,89,54,14,3,24,68,90]
end1=list(map(lambda a:a%2!=0,start1))
print(end1)


ax=["Air", "Filter", "Birth", "Earth", "Unavailable", "Idea", "Logical"]
bx=['a','e','i','o','u']
div=list(filter(lambda ab:ab[0].lower() not in (bx),ax))
print(div)
