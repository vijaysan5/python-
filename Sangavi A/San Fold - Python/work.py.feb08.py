"""a=34
b=45
if(a<b):
    print("b is greater than a")
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

a=int(input("Age:"))
b=str(input("Vote Place Num.: "))
c=18
d="M07" and "M09" and "M12"
if(c<a) and (d==b):
    print("Vote is Accepted")
else:
    print("Vote is Not Accepted")


a=int(input("x:"))
print(a)
b=(a**a)
print(b)
if(a%2==0):
    print("This is Even Number")
else:
    print("This is odd Number")

a=int(input("Tamil: "))
b=int(input("English:"))
c=int(input("Hindi:"))
if(a>45) and (b>35) and (c>25):
    print("Pass")
else:
    print("Fail")
-------------------------------------
Tam=85
Eng=78
if(Tam>85) and (Eng>85):
    print("Above 85 to 99")
elif(Tam>70) and (Eng>70):
    print("Above 70 to 85")
else:
    print("not Valid this mark")
----------------------------------------
Area=35
Location="Karaikal"
if(Area<29):
    print("Area is Valid")
    if(Location=="Karaikal"):
        print("Location is Correct")
    else:
        print("Not Located")
else:
    print("Area is not Valid") 
print("________________________________")
Area=int(input("Vote:"))
Age=int(input("Age:"))
Loc=str(input("Location:"))
Loc1="Madurai"
if(Area>250):
    print("Area is selected")
    if(Age>25):
        print("Age is Valid")
    else:
        print("Age is Not Valid")
        if(Loc1==Loc):
            print("Loc is Correct")
        else:
            print("Loc is wrong")
else:
    print("Area, Age and Loc. also Selected for Vote")
"""
a=str(input("Name:"))
b=int(input("Age:"))
if(b>18):
    print("Age is Valid")
    sub1=int(input("tam:"))
    sub2=int(input("eng:"))
    sub3=int(input("phy:"))
    sub4=int(input("zoo:"))
    sub5=int(input("bot:"))
    sub6=int(input("che:"))
    x=(sub1+sub2+sub3+sub4+sub5+sub6)
    print(x)
    ave=x/6
    if(x>450):
        print("Student is Qualified")
        if(ave>90.0):
            print("student is Qualified to mbbs")
        else:
            print("student is not Qualified to mbbs")
            if(ave>80.0):
                print("student is Qualified to engin..")
            else:
                print("student is not Qulified to engin.")
    else:
        print("student is not Qualified")
else:
    print("age is not valid")
    


        
