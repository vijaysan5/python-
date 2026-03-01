print("login details")
print("1.user login \n2.customer login")

# ud=open("order data.txt","x")
def repeat():
    login=int(input("enter your chooise"))
    users=['Arun','Ajith','Vijay','Suriya','Simbu']
    password="Company@1.in"
    if login==1:
        uname=str(input("enter your name:")).capitalize()
        passw=input("enter the password:")
        if ((uname in users) and (passw == password)):
            def usr():
                sproduct=str(input("sold Product=")).capitalize()
                scount=int(input("sales count="))
                sprice=int(input("sales price="))
                return f"{uname}-user\nsold Produc:{sproduct}\nsales count:{scount}\nsales price:{sprice}\n\n"
            with open("order data.txt", "a") as osd:
                osd.write(usr())
        else:
            print("username or password incorrect")
    elif login==2:
        def cus():
            cname=str(input("register your name:")).capitalize()
            oproduct=str(input("your ordered product=")).capitalize()
            price=int(input("enther the price="))
            quantity=int(input("enter the quantity="))
            remarks=str(input("remarks=")).capitalize()
            return f"{cname}-customer\nyour ordered product:{oproduct}\nprice:{price}\nquantity:{quantity}\nremarks:{remarks}\n\n"
        with open("order data.txt", "a") as ocd:
            ocd.write(cus())
    else:
        print("invalid chooise")
repeat()

rep=str(input("another entry? y/n"))
if rep=="y":
    repeat()
else:
    print("updation complete")

with open("order data.txt", "r") as rod:
    print(rod.read())