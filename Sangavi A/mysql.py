import pymysql as mysql


dataBase = mysql.connect(
  host ="localhost",
  user ="root",
  passwd ="password"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE company")


connect=mysql.connect(host="localhost",user="root",password="password",database="company")
curser=connect.cursor()

curser.execute("select * from employee")
details=curser.fetchall()
# print(details)

columns=[col[0] for col in curser.description]
# print(columns)

curser.execute("insert into employee(sname,age,salary,did) values('banu','26','34000','3')")
curser.execute("update employee set salary=29500 where sname='harish'")
curser.execute("select * from employee where sname like 'a%'")
a=curser.fetchall()
curser.execute("select * from employee where sname like 'b%'")
b=curser.fetchall()
print(a,b,sep='\n')

""" import pymysql as mysql

con=mysql.connect(host='localhost',user='root',password='livewire',database='company')
cursor=con.cursor()

cursor.execute("""
# CREATE TABLE IF NOT EXISTS emp_details(
#                sno INT AUTO_INCREMENT PRIMARY KEY,
#                name VARCHAR(200),
#                email VARCHAR(250),
#                phone VARCHAR(100)) 
""")
cursor.execute("ALTER TABLE emp_details MODIFY COLUMN email VARCHAR(250) NULL")
cursor.execute("ALTER TABLE emp_details MODIFY COLUMN phone VARCHAR(100) NULL")

def insert_values(name,email,phone):
    cursor.execute("INSERT INTO emp_details (name,email,phone) VALUES (%s,%s,%s)",(name,email,phone))
    con.commit()
    print("data inserted successfully")

def show_data():
    cursor.execute("select * from emp_details")
    data=cursor.fetchall()
    for i in data:
        print(i)

def get_data_by_phone(phone):
    cursor.execute("select * from emp_details where phone=%s",(phone,))
    print("successfully get the data")
    data=cursor.fetchone()
    print(data)

def update_email(email,name):
    cursor.execute("update emp_details set email=%s where name=%s",(email,name))
    cursor.execute("select * from emp_details")
    print("updated succesfully")
    data=cursor.fetchall()
    for i in data:
        print(i)
def delete_using_name(name):
    cursor.execute("delete  from emp_details where name=%s",(name,))
    print("deleted successfully")
    cursor.execute("select * from emp_details")
    data=cursor.fetchall()
    for i in data:
        print(i)

# insert_values("hendry", "hen36@gmail.com", "6895346798")
show_data()
get_data_by_phone("1234567890")
update_email('benjamin@gmail.com','ben ten')
delete_using_name('ben ten') """