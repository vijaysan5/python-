'''def abc(x):
    for a in range(x):
        if a%2==1:
            continue
        print(a)
abc(25)    
def any(a):
    x=0
    while a>0:
        b=a%10
        x=x*10+b
        a//=10
    print(x)
any(int(input("value:")))
'''        
'''
a={"b":1,"d":2,"c":3}
for i,j in a.items():
    print(f"{i} == {j}")
    print("{} == {}".format(i,j))
'''
'''b=("Hey","Welcome")
for i in b:
    print(i)
'''
'''
x,*y=23,34,24
print(x,y)

def san(ak, *bk, **ck):
    print("Txt:", ak)
    print("Txt*:", bk)
    print("Txt**:", ck)
san("Disk", "Hp", "Ssd", "samT", akk = 23 , skk = 25)

def vi(*NumI, **NumII):
    print("Hello:")
    for I in NumI:
        print(I)

    print("Hi World")
    for II,IJ in NumII.items():
        print(f"{II}=={IJ}")

vi("long", "live", "skip", "turn", cm=523, km="200m")

x={"a":32,"b":51,"c":89}
for a in x:
    print(a)
    
for c,d in x.items():
    print(c,d)
for sa,vs in x.items():
    print(f"{sa}=={vs}")'''

def v(sa,sv,sy):
    return (sa+sv+sy)
value=[23,35,51]
enter = v(*value)
print(enter)

def s(a,b,c):
    return (a,b,c)
v = (1,3,5)
ef = s(*v)
print(ef)

