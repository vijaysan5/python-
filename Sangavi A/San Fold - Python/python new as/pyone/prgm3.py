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
