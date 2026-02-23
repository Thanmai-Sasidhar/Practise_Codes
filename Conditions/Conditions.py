'''#Conditions

#Coming to 'if-elif-else' there are if ,if-else ,if elif, if-elif-else ,if elif.., Nested if

#USING COMPARISON OPERATOR --- [ >,<,>=,<=,!=,== ]

a,b=10,20
if a<b:
    print("B is Greater")

if a>b:
    print("A is Greater")

if a<=b:
    print("True")

if a>=b:
    print("True")

a,b=4,4
if a==b:
    print("True")

a,b=2,4
if a!=b:
    print("True")

name=input() 
if name =="sasi":
    print("Valid")

a="Python"
if a="python":
    print("True")

a=int(input("Enter a value:"))
if a>40:
    print("Greater")

a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
if a>b:
    print("A is Greater")    

#USING LOGICAL OPERATOR -- [and ,or ,not ]

a=5,b=9

if a<b and b>a:
    print("a is Less")

if a!=b and a==b:
    print("Less")#It will not be executed

if a<b or b>a:
    print("a is Less")

if a!=b or a==b:
    print("Less")#It will be executed

if not b>a:
    print("B is Less")

if not a==b:
    print("Both are Different")  

#USING IDENTITY OPERATOR

a=10
if a is type(int):
    print("Integer")

a=10
if a is not type(int):
    print("Not an Integer")    

b=10.0
if b is type(float):
    print("Float")

b=10.0
if b is not type(float):
    print("Not a Float")

c=True
if c is type(bool):
    print("Its a Bool")

c=False
if c is not type(bool):
    print("Not a Bool")    

d=2j+1
if d is type(complex):
    print("Complex")

d=2j+1
if d is not type(complex):
    print("Not a Complex")     

e="2j+1"
if e is type(str):
    print("String")

e="2j+1"
if e is not type(complex):
    print("Not a String")

#Example in Runtime
a=input()
print(type(a))
if type(a)==str:
    print("Integer")

#USING MEMBERSHIP OPERATORS

a=[1,2,3,4,5,6,7,8,9]
if 2 in a:
    print("True")

a=[1,2,3,4,5,6,7,8,9]
if 2 not in a:
    print("True")

a=[1,2,3,4,5,6,7,8,9]
if 20 in a:
    print("True")

a=list(map(int,input().split()))
if 2 in a:
    print("True")

a=[10,20,30,40,50]
b=int(input())
if b in a:
    print(b)

a=input()
if "2" in a:
    print("True")
'''
