#ASCII TASKS 
''' 
for i in range(65,91):
    print(chr(i),end=" ")

print()

for i in range(97,123):
    print(chr(i),end=" ")

print()

name="SASIDHAR"
for i in name: 
    print(ord(i),end=" ")
'''

#Anonymous Functions

'''
Annonymous Functions are nameless functions we use a keyword called as 'lambda' to create annnonymous functions
'''

#Write a function to calculate 2*x+5
'''
def cal(x):
    a=(2*x)+5
    return a
        
x=5
print(cal(x))       
'''

#Syntax  --->  a=lambda : expression
'''
x=5
a=lambda x:2*x+5
print(a(5))
'''
'''
a=int(input())
b=lambda x:2*x+5
print(b(a))
'''

#TASKS

#Multiply 2 numbers
'''
a=int(input("Enter the Value of a : "))
b=int(input("Enter the value of b : "))

c=lambda x,y:x*y
print(c(a,b))
'''

#Convert string to uppercase
'''
a="python"
b=lambda x:x.upper()
print(b(a))

b=lambda x:x.upper()
print(b("python"))
'''

#Fname and Lname

'''
f=input()
l=input()
c=lambda x,y:x+" "+y
print(c(f,l))
'''
#using generators method
'''
a,b=[i for i in input("Enter the Value ").split(",")]
c=lambda x,y:x+" "+y
print(c(a,b))
'''

#filter()

#SYNTAX --->>>  fliter(lambda expression || Data Type , list varibale)

a=[2,3,5,7,8,9,11,20,30,40,None]
'''
for i in a:
    if i%2==0:
        print(i)
'''
'''
b=list(filter(lambda x:x%2==0,a))
print(b )
'''
'''
b=list(filter(lambda x:x==None,a))
print(b)
'''
'''
b=list(filter(None,a))
print(b)
'''

#map() ---> Each object from a collection and forms a new collections
'''
a=[10,5,6,7,5,4,1,2]
b=[12,21,23,43,53,1,2,3]

c=list(map(max,a,b))
print(c )
'''
'''
a=[10,5,6,7,5,4,1,2]
b=[12,21,23,43,53,1,2,3]

c=list(map(min,a,b))
print(c )
'''
 
