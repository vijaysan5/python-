# co = open("company.txt","x")

""" wr = open("company.txt", "w+")
wr.write("company Name: Meta \n\n")

ap = open("company.txt", "a+")
ap.write("Owner: Mark \n")
ap.write("Age: 46 \n\n")

ap.write("Manager: Arun \n")
ap.write("Salary: 10000000 \n")
ap.write("W Hours: 8 \n\n")

ap.write("Epm Delails: \n")
ap.write("Name \t Salary \t W Hours \n")
ap.write("Arvin \t 500000 \t 9 \n")
ap.write("Arjun \t 505000 \t 9 \n")
ap.write("Gobi \t 499000 \t 9 \n")
ap.write("Maya \t 510099 \t 9 \n")
ap.write("Gokul \t 905000 \t 9 \n")
ap.write("Rahul \t 340500 \t 9 \n")
ap.write("Raj \t 800000 \t 9 \n")
ap.write("Ram \t 556400 \t 9 \n") """


rd = open("company.txt", "r+")
# rd.seek(0,0)
# print(rd.read())
# print(rd.readline())

name=rd.read(14)
print(name,"\n",rd.readline())

rd.seek(30)
print("Owner: \n",rd.readline())

rd.seek(42)
print("Owner Age: \n", rd.readline())

rd.seek(58)
print("Manager: \n", rd.readline())

rd.seek(73)
print("manager Salary: \n", rd.readline())

rd.seek(93)
print("Manager Working Hour: \n", rd.readline())

rd.seek(140)
emp = rd.readlines()

for i in emp:
    parts = i.strip().split('\t')
    name = parts[0].strip()
    salary = parts[1].strip()
    hours = parts[2].strip()
    print(f"name: {name} \nsalary: {salary} \nhours: {hours} \n")
       