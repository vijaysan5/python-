"""print("Feb 09")
#if
a=20
b=25
if(a<b):
    print("a is less than b")
print("--------------------------------------")
#else
a=40
b=53
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")
print("--------------------------------------")
#elif
a=73
if(a>90):
    print("above 90")
elif(a>80):
    print("above 80")
elif(a>70):
    print("above 70")
else:
    print("not valid this value")
print("--------------------------------------")
#nested if
a=str(input("Name:"))
b=int(input("Age:"))
if(b>21):
    print("Age is valid for this Exam")
    sem1=int(input("sem:"))
    sem2=int(input("sem:"))
    sem3=int(input("sem:"))
    sem4=int(input("sem:"))
    x=(sem1+sem2+sem3+sem4)
    print(x)
    Ave=x/4
    if(Ave>90.0):
        print("stu. Qualified to JRF")
    else:
        print("stu. not Qualified to jrf")
        if(Ave>81.5):
            print("stu. Qualified to Ass. Prof.")
        else:
            print("stu. Not Qualified to Ass. Prof.")
            if(Ave>70.0):
                print("stu. Qualified to Ph.d")
            else:
                print("stu. Not Qualified")
else:
    print("Age is Not valid for this Exam")

a=str(input("Name: "))
Tam=int(input("Tamil:"))
Eng=int(input("English:"))
Math=int(input("Maths:"))
Sci=int(input("Science:"))
Soc=int(input("Social:"))
b=int(Tam+Eng+Math+Sci+Soc)
print(b)
if(b>(450)):
    print("'O' Gread")
elif(b>(400)):
    print("'A' Gread") 
elif(b>350):
    print("'B' Gread")
if(b>300):
    print("'C' Gread")
elif(b>250):
    print("'D' Gread")
else:
    print("Stu. is fail")
a=str(input("Name:"))
b=int(input("Age:"))
c=str(input("Qualification:"))
d=str(input("Distric: "))
x=25
x1=40
y="Diploma"
y1="Any Degree"
z="Mayiladuthurai"
if(b>x) and(b<x1):
    print("Age is Valid")
    if(c==y) or (c==y1):
        print("Education is Valid")
        if(z==d):
            print("Dis. is Valid")
else:
    print("Age is Not Valid")"""
A=str(input("name: "))
B=float(input("Percentage:"))
C=70.5
D=50.8
if(B>C):
    print("Eligible for Paper 2 exam")
    if(B>D):
        print("Eligible for paper 1 Exam")
else:
    print("Not Eligible for this exam")
