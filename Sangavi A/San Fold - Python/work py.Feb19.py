def vj(NumI, *NumII, **NumIII):
    print("Txt1:",NumI)
    print("Txt2:",NumII)
    print("Txt3:",NumIII)
vj("ABC", "BCD", "CDE", "DEF", "EFG", Place="Budhapast", Name="Yash", Age=21)

def vi(Sanv,*San,**SanI):
    for san in Sanv:
        print(san,sep="_")
    
    for I in San:
        print(I)
   
    for A in SanI:
        print(A)
    
    for X,Y in SanI.items():
        print(f"{X}=*={Y}")
vi("lovely", "Happy", "Smile", "Nice", "Cute", Place="Budhapast", Name="Yash", Age=21)


x={21:"A", 23:"B", 25:"C", 29:"D"}
for a in x:
    print(a)

for c,d in x.items():
    print(f"{c}='_'={d}")

for e,f in x.items():
    print(e,f)
    
def vy(ab, cd, ef):
    return (ab+cd+ef)
value=[23,25,29]
ani=vy(*value)
print(ani)

