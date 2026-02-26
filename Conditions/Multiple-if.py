'''#Multiple if
a=5
b=10

if a<b:
    print("less")
if b>a:
    print("Greater")
if a!=b:
    print("Not Equal") # Here all the statements are printed because all are valid

a=5
b=10

if a<b:
    print("less")
elif b>a:
    print("Greater")
elif a!=b:
    print("Not Equal") #Here only if one statement is true that is printed
    
a=5
b=10

if a==b:
    print("less")
if b>a:
    print("Greater")
if a!=b:
    print("Not Equal") # Here the 2 correct statements are printed 

a=5
b=10

if a==b:
    print("less")
if b>a:
    print("Greater")
if a==b:
    print("Not Equal")
elif(a!=b):
    print("True")

#USING LOGICAL OPERATORS

a=5
b=10

if a!=b and b>a:
    print("less")
if b>a or a==b:
    print("Greater")
if not :
    print("Not Equal")

#USING MEMBERSHIP

a=[1,2,3,4,5]
b=5

if b in a:
    print("Valid")
if a not in b:
    print("In Valid")

#Using Identity
    
a=5
b=10.4

if type(a) is int:
    print("True")
if type(b) is not int:
    print("True")

a=[3,4,5,6,7,8,9]
if 3 in a:
    print("true")
if 10 not in a:
    print("fasle")

'''


    

    
    
    
