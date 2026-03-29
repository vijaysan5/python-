#Error and Exception:
'''
try:
    value=int(input("abc:"))
    divide= 50/value
    print(divide)       #(abc:5)=10.0
except ZeroDivisionError as a: 
    print(a)            #(abc:0)=division by zero
except ValueError as b:  
    print(b)            #(abc:san)=invalid literal for int() with base 10: 'san'

try:
    value_1=int(input("ab:"))
    value_2=int(input("xy:"))
    Total= value_1 / value_2
    print(Total)
except ZeroDivisionError:
    print("Error >< Zero Divide error")
except ValueError:
    print("Error >< Value is error")
finally:
    print("Completed")
'''

def San(ab):
    assert (ab>=20), "sanv"  #: True or False  or assert (ab>=20), "sanv"
    return (ab%2==0), "Hello"
print(San(24))

def San_2(ab,xy):
    if xy==0:
        raise ValueError("Error: Value")
    return ab / xy
#print(San_2(23,0))>>>raise ValueError("Error: Value")><ValueError: Error: Value
#print(San_2(24,4)) #6.0
try:
    EFG= San_2(20,0)
except ValueError as a:
    print(a)        #xy==0___ so output>>>"Error: Value"


try:
    ABC= San_2(44,4)
except ValueError as b:
    print(b)        #xy!=0___so this not show on output sheet.
print(ABC)          #11.0









    
