# 0001. Single Inheritance :
## No.01
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')
ab=Blue("Krishnan", "Yazh")
ab.san()

class Girl(Blue):
    pass

ac=Girl("Vishnu", "Dhiya")
ac.san()"""
## No.02
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')

class Girl(Blue):
    def __init__(self, NameOne, NameTwo):
        Blue.__init__(self, NameOne, NameTwo)

xy=Blue("Krishnan", "Yazh")
xy.san()"""
## No.03
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')

class Girl(Blue):
    def __init__(self, NameOne, NameTwo):
        super().__init__(self, NameOne, NameTwo)

abc=Blue("Krishnan", "Yazh")
abc.san()"""


# 0002. Multiple Inheritance :
"""class Add:
    def __init__(self, ab, xy):
        self.a = ab
        self.x = xy
    def Adding(self):
        return self.a + self.x

class Multiple:
    def __init__(self, ab, xy):
        self.a = ab
        self.x = xy
    def Multix(self):
        return self.a * self.x

class Add_and_Multiple(Add, Multiple):
    def __init__(self, ab, xy):
        self.a =ab
        self.x = xy
    def  Class_Add_Multi(self):
        Addition = Add.Adding(self)
        Multiplication = Multiple.Multix(self)
        return (Addition, Multiplication)
    
ABC = Add_and_Multiple(3,5)
print("Add:", ABC.Adding())
print("Multiplication:", ABC.Multix())
print("Add & Multix:", ABC.Class_Add_Multi())"""

    
# 0003. Multi level Inheritance :
"""class User_One:
    def User_One(self):
        print("Good Morning to All...!")
class User_Two(User_One):
    def User_Two(self):
        print("Have a Beautiful Day *_*")
class User_Three(User_Two):
    def User_Three(self):
        print("How is going Today?")

Users = User_Three()

Users.User_One()
Users.User_Two()
Users.User_Three()"""


# 0004. Hierarchical Inheritance :
"""class san_v:
    def san_v(self):
        print("Welcome")
class san_one(san_v):
    def san_one(self):
        print("Student number One_1")
class san_two(san_v):
    def san_two(self):
        print("Student number two_2")
Name_1 = san_one()
Name_2 = san_two()

Name_1.san_v()
Name_1.san_one()
Name_2.san_v()
Name_2.san_two()
"""


# 0005. Hybrid Inheritance :
##___01 :
"""class Blue:
    def __init__ (self, RollNumber):
        self.RollNumber = RollNumber
    def san (self):
        print(f'{self.RollNumber}')

class Girl(Blue):
    def girl(self):
        print(f'{self.RollNumber}')
    
class PlayWell:
    def __init__(self, Word):
        self.Word = Word
    def Play(self):
        print("Well Played")

class NewPlay(Girl, PlayWell):
    def new(self):
        self.girl()
        self.Play()

Name_1 = NewPlay("4385")
Name_1.new()"""
##___02 :
"""class FileHandle:
    def Name(self):
        print("Name is Selected")

class sana:
    def __init__ (self, Mean):
        self.Mean = Mean
    def yazh(self):
        print(f'{self.Mean}')
class visible(sana):
    def __init__(self, Mean):
        super().__init__(Mean)
    def seen(self):
        print(f'{self.Mean}')

class Wellwiz(FileHandle, visible):
    def livein(self):
        self.Name()
        self.seen()
Username = Wellwiz("Happy Forever")
Username.livein()"""



