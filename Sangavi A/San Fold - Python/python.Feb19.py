user=25
def san():
    pas=14
    print(user)
    print(pas)
san()

def sanv():
    c=21
    print(user)
    print(c)
sanv()
print(user)

def win():
    global user
    user=23
    print(user)
win()

def swe(s):
    if s == 0:
        return 1
    else:
        return s * swe(s- 1)
print(swe(9))

def recv(vs):
    if vs>0:
        return 1
    else:
        return vs+recv(vs-2)
print(recv(21))


