
def wish():
    print("Happy Birthday Sista")
wish()

def numfind(x):
    if x%2==0:
        return "Even Num"
    else:
        return "Odd Num"
print(numfind(int(input("x: "))))
print(numfind(int(input("x: "))))

def value (x,y=23):
    print("a:", x)
    print("b:", y)
value(int(input("x:")))

def NameAge(Name,Age):
    print(Name,Age)
NameAge(Name=str(input("Name:")),Age=int(input("Age:")))

def Location(Name,Place):
    print("Hi Mam. My Name is:",Name)
    print("I'm from:",Place)
Location(Name=str(input("Name:")),Place=str(input("Place:")))
"""
"""
def y(x):
    for a in range(x):
        if a%2==0:
            continue
        print(a)
y(23)

def value(x):
    z=0
    while x>0:
      y=x%10
      z=z*10+y
      x//=10
    print(z)
value(int(input("k:")))

def number(t):
    v=0
    while t>0:
        u=t%10
        v=v*10+u
        t//=10
    print(v)
number(int(input("enter:")))
        
