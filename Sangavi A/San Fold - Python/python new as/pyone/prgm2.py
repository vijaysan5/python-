'''def san (x,y):
    if x>y:
        print("True")
    else:
        print("False")

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
'''
def self():
    Name=str(input("Name:"))
    Age=int(input("Age:"))
    Location=str(input("Address:"))
    def detailz():
        return Name,Age,Location
        if Age>18:
        print("Age is Valid")
        Tam=int(input("Tam:"))
        Eng=int(input("Eng:"))
        Zoo=int(input("Zoo:"))
        Bot=int(input("Bot:"))
        Phy=int(input("Phy:"))
        Che=int(input("Che:"))
        Total=(Tam+Eng+Zoo+Bot+Phy+Che)
        print(Total)
        if Tam>35 and Eng>35 and Zoo>35 and Bot>35 and Phy>35 and Che>35:
            print("Student is Qualified")
            if Total>550:
                print("Qualified to MBBS")
            elif Total>500:
                print("Qualified to Micro.Bio")      
            elif Total>400:
                print("Qualified to Nursing")
        else:
            print("Strudent is not Qualified")
    else:
        print("Age is not Valid")

self()
detailz()
