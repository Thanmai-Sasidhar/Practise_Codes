'''#Conditions

#Coming to 'if-elif-else' there are if ,if-else ,if elif, if-elif-else ,if elif.., Nested if

#USING COMPARISON OPERATOR --- [ >,<,>=,<=,!=,== ]

a,b=10,20
if a<b:
    print("B is Greater")
else:
    print()
 
a,b=3,9
if a>b:
    print("A is Greater")
else:
    print("B is greater")

a,b=10,20
if a<=b:
    print("A is less than or equal to B")
else:
    print("A is Greater")

a,b=3,9
if a>=b:
    print("A is Greater than or equal to B")
else:
    print("B is Greater")

a,b=10,20
if a==b:
    print("A and B are Equal")
else:
    print("A and B are not Equal")

a,b=3,9
if a!=b:
    print("A and B are not Equal")
else:
    print("A and B are Equal")

a=int(input())
b=int(input())

if a>b:
    print("A is Greater")
else:
    print("A is Lesser")

#USING LOGICAL OPERATOR ---[and, or, not]   

a=6
b=12
if a>b and b>a:
    print("True")
else:
    print("False")

if a!=b or a==b:
    print("True")
else:
    print("False")

if not a>b:
    print("True")
else:
    print("False")

a=int(input())
b=int(input())
if not a>b:
    print("True")
else:
    print("False")
      
    
#USING IDENTITY OPERATOR ---[is ,is not]   

a=6
b=12
if a:
    print("True")
else:
    print("False")

if a!=b or a==b:
    print("True")
else:
    print("False")

if not a>b:
    print("True")
else:
    print("False")

a=int(input())
b=int(input())
if not a>b:
    print("True")
else:
    print("False")

#USING IDENTITY OPERATOR

a=10
if a is type(int):
    print("Integer")
else:
    print("Not of Valid Type")

a=10
if a is not type(int):
    print("Not an Integer")
else:
    print("Not of Valid Type")    

b=10.0
if b is type(float):
    print("Float")
else:
    print("Not of Valid Type")    

b=10.0
if b is not type(float):
    print("Not a Float")
else:
    print("Not of Valid Type")    

c=True
if c is type(bool):
    print("Its a Bool")
else:
    print("Not of Valid Type")
    
c=False
if c is not type(bool):
    print("Not a Bool")    
else:
    print("Not of Valid Type")
    
d=2j+1
if d is type(complex):
    print("Complex")
else:
    print("Not of Valid Type")
    
d=2j+1
if d is not type(complex):
    print("Not a Complex")     
else:
    print("Not of Valid Type")
    
e="2j+1"
if e is type(str):
    print("String")
else:
    print("Not of Valid Type")

e="2j+1"
if e is not type(complex):
    print("Not a String")
else:
    print("Not of Valid Type")
    
#Example in Runtime
a=input()
print(type(a))
if type(a)==str:
    print("Integer")
else:
    print("Not of Valid Type")    

#USING MEMBERSHIP OPERATORS

a=[1,2,3,4,5,6,7,8,9]
if 2 in a:
    print("True")
else:
    print("False")    

a=[1,2,3,4,5,6,7,8,9]
if 2 not in a:
    print("True")
else:
    print("False")    

a=[1,2,3,4,5,6,7,8,9]
if 20 in a:
    print("True")
else:
    print("False")    

a=list(map(int,input().split()))
if 2 in a:
    print("True")
else:
    print("False")    

a=[10,20,30,40,50]
b=int(input())
if b in a:
    print(b)
else:
    print(a)    

a=input()
if "2" in a:
    print("True")
'''

a=int(input())
b=int(input())

if type(a) is not int:
    print("False")
else:
    print("True")
#elif using LOGICAL     
a,b=6,8
if a<b:
    print("B Greater")
elif b==a:
    print("Equal")
else:
    print("False")

a=int(input())
b=int(input())

if a>b:
    print("A is greater")
elif a==b:
    print("EQUAL")
else:
    print("B is greater")

#Logical
a=10
b=20

if a>b and b>a:
    print("True")
elif a>b or b>a:
    print("True")
elif not (b>a):
    print("True")
else:
    print("False")

#Identity
a=10
b=20

if :
    print("True")
elif a>b or b>a:
    print("True")
elif not (b>a):
    print("True")
else:
    print("False")

    


    
    
