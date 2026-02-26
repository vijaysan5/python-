def san(a,c=2):
    print(a/c)

user=23
def ab():
    pasw=21
    print(user+pasw)

def ac(x):
    print(user-x)

def ad(y,z):
    count=y+z
    print(count%2)

inuse=8
def now(b):
    userin=5
    a=(inuse//userin)
    print(a*b)
    
def new(xy):
    global inuse
    inuse=2
    print(inuse**xy)

def joy(name,place):
    print("Name:", name)
    print("Place:", place)

def sana(a,b):
    if a>b:
        print("True")
        if a%2==0:
            print("it's a Even num")
    else:
        print("False")
    
def sandra(a,b,c,d):
    if a>35 and b>35 and c>35 and d>35:
        print("Pass")
    else:
        print("Fail")

def ik(xa,xb):
    print("a" in xa)
    print("v" not in xb)

ainput=50
def finance(cv):
    b=(int(input("mn:")))
    if ainput==cv:
        print("Equal")
        if ainput>b:
            print("True")
        else:
            print("False")
    else:
        print("It's not Equal")

def location():
    Name=str(input("Name:"))
    Doornum=int(input("No:"))
    Area=str(input("Area:"))
    Dt=str(input("Dt:"))
    return Name, Doornum, Area, Dt

    
    
