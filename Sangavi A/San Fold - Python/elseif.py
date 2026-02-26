#else if

a=90
if (a>85):
    print("85")
elif (a>80):
    print("80")
elif(a>75):
    print("75")
else:
    print("Else")

#nested if

age=45
place="madurai"

if(age>18):
    print("Age valid")
    if(place=="madurai"):
        print("Place also valid")
    else:
        print("Place is not valid")
else:
    print("Age is not valid")
