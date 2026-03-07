san = {
    "Name": "Dhiya",
    "Age": 23}
print(san)

san_1={
    "Name": "Dhiya",
    "Age": 23,
    "Year":2003,
    "Year":2005}
print(san_1)
print(san_1["Name"])

#keys_values_items
san_2=dict(Name="Kajal", Age=21, Place="Madurai", GEmp= True)
print(san_2)
print(san_2["Name"])
asv=san_2
print(asv)

x=asv.keys()
y=asv.values()
z=asv.items()
print(x)
print(y)
print(z)

Enf={
    "Name":"Yazh",
    "Age":23,
    "Place":"Madurai",
    "C.Year":2023,
    "C.Year":2025
    }
print(Enf)
print(Enf["C.Year"])
Enf["BirthY"]=2002
print(Enf)

#update_pop_del_popitem_clear
Enf.update({"BirthM":"March"})
print(Enf)
Enf.pop("C.Year")
print(Enf)
del Enf["Place"]
print(Enf)
Enf.popitem()
print(Enf)
Enf.clear()
print(Enf)

#Nested dict
Fruits={
    "Berry":{
        "Plant Num" : 5,
        "Week 1" : 298,
        "Week 2" : 279},
    "Cherry":{
        "Plant Num" : 8,
        "Week 1" : 349,
        "Week 2" : 299},
    "Blackcurrent":{
        "Plant Num" : 3,
        "Week 1" : 793,
        "Week 2" : 789}
    }
print(Fruits)
print(Fruits["Berry"]["Plant Num"])
print(Fruits["Blackcurrent"]["Week 1"],["Week 2"])

for x in Fruits.values():
    print(x)
for y in Fruits.keys():
    print(y)
for x,y in Fruits.items():
    print((x),end="_")
    print(y)

saha={
    "Name" : "Dhanvi",
    "DOB" : "March 15th",
    "Year" : 1998
    }
print(saha)

Dhanvi=saha.copy()
print(Dhanvi)
Dharani=Dhanvi.fromkeys(["Name"],["Dharani"])
Dharani_2=Dhanvi.fromkeys(["DOB"],["December 21st"])
print(Dharani,end="_-_-_")
print(Dharani_2)

