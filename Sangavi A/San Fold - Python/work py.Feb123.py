a=0
while (a<5):
    print("a")
    a+=1   
for a in range(1, 5):
    print(a)
print("------------------------")
for b in range(1, 23, 2):
    print(b)
print("------------------------")
for x in range(0, 50, 5):
    print(x)


d="Location"
for x in range(len(d)):
    print(x)
a=["Locatin", "I am"]
b=["from Madurai", "from Chennai", "from Karaikal"]   
for y in a:
    for z in b:
        print(y,z)
print("------------------------------------------")
a=["Locatin", "I am", "Are you"]
b=["from Madurai", "from Chennai", "from Karaikal"]
for d in a:
    if d == "Are you":
        break
    print(d)
    for e  in b:
        if e == "from Chennai":
            continue
        print(e)
print("------------------------------------------")  
for x in range(15):
    if x == 3:
        continue
    print(x)
    print("============")
    if x == 5:
        break
    print(x)
    print("______________")

