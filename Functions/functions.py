#functions

#1.A function is a block of organized and reuasble code which is used to perfrom a single or multiple tasks
#2.Python gives inbuilt functions like print and u can make ur own function also and these are called user-defined functions
#3.Function block begin with the keyword def and followed by function name followed by paranthesis ()
'''
a=10
b=20
print("THE SUM IS :",a+b)
print("THE DIFFERENCE IS :",a-b)
print("THE PRODUCT IS :",a*b)
'''
'''
def cal(a,b):
    print("The Sum is :",a+b)
    print("The Difference is :",a-b)
    print("The Product is :",a*b)
cal(10,20)
'''
'''            
def cal(a,b):
    print("The Power is :",a**b)
    print("The Modulus is :",a%b)
    print("The Integer Division is :",a//b)
cal(10,20)
'''
'''
def add(a,b):
    print(a+b)
add(5,6)    
'''
'''
def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()
'''
'''
def fullname():
    fname=input()
    lname=input()
    print((fname+" "+lname).title())
fullname()
'''

#DIFFERENCE BW PRINT AND RETURN

#1.print just shows the human user output in a console
#2.return is used to terminate the function and gives back a value from the function

#print vs return
'''
def mul(a,b):
    print(a*b)
mul(3,4)
'''
'''
def mul(a,b):
    return a*b
print(mul(2,3))
'''
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,4))
'''
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,4))
'''
#TASK 1

#Method 1
'''
def funct():
    a=int(input("Enter the a value: "))
    b=int(input("Enter the b value: "))
    print("---------------------\n1= Addition\n2= Subtraction\n3= Multiplication\n4= Division\n-------------------")
    option=int(input("Enter the option number:"))
    if option==1:
        return a+b
    elif option==2:
        return a-b
    elif option==3:
        return a*b
    elif option==4:
        return a/b
    else:
        return "You have Entered Wrong Option...!"
print(funct())    
'''

#Method 2
def add():
    print(a+b)      
def sub():
    return a-b
def multiply():
    return a*b

while True:
    a=int(input())
    b=int(input())
    option=int(input('''Choose the option 1.Add\n2.Sub\n3.Multiply'''))
    if option ==1:
        add()
    elif option==2:    
        sub()
    elif option==3:
        multiply()
'''



