# GLOBAL AND LOCAL VARIABLES
 
## A Variable insode and outsid the function is called global and local variables

## A varible define above the function and is accessible to the entire global space is called GLOBAL VARIABLE

## A varibale inside the function is called LOCAL VARIABLE

#First Case of Global Variable
'''
a=3
def check():
    print("Inside Value :",a)
check()
print("Outside Value :",a)
'''
#Second case of Global Variable
'''
a=2
def check():
    a=5
    a=a**2
    print("Inside Value: ",a)
check()
print("Outside Value :",a)
'''
#Third case of both global and local variable
'''
a=4
b=3

def check():
    a=7
    print("Inside value is ",a)
    a=10
    print("Updated Value: ",a)
    b=12
    b=b+a
    print("Value of b is : ",b)
check()
print("A's value is :",a)
print("B's value is :",b)
'''
#USAGE OF GLOBAL KEYWORD --->
'''
When user wants to access the global variable inside the function directly and carry forward the updated value
even outside the function then we need to use the global keyword. 
'''
'''
a=5
def final():
    global a
    print("a value is :",a)
    a=10
    print("Updated value of a: ",a)
    global b
    b=15
    b+=a
    print("The value of b is :",b)
final()
print("The value of a is :",a)
print("The value of b is :",b)
'''

#Generators

'''
No tuple Comprehension in above cases if we remove those braces and keep paranthesis then the outcome is
Generator
'''
'''
If we replace [] with () then it will be tuple comprehension

list comprehension = [expression for variable in collection/range]

While using generator we should use * to unpack the elements
'''
'''
a=[i for i in range(10)]
print(a)
print(type(a))
'''
'''
a=(i for i in range(10))
print(a)
print(type(a))
'''
'''
a=(i for i in range(10))
print(*a)
print(type(a))
'''
'''    
a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
#print(set(a))
'''
#DEFINITION OF GENERATOR
'''
A generator is also a function which can be used as an iterator(loop) by producing group of values where we use
yield keyword
'''

#yield vs return
'''
return will terminate the function and where as yield can pass the function and go on with every successive iteration
'''

#Taking multiple inputs in one line
'''
a,b=[int(i) for i in input("Enter the Value ").split(",")]
def check(a,b):
    while a<b:
        yield a 
        a+=1
        yield a

print(*check(a,b))
'''
'''
a,b=[int(x) for x in input("Enter the Values: ").split(",")]
def check(a,b):
    while a<b:
        a+=1
        #return a
    return a
print(check(a,b))
'''
#yield vs return

#simple ga return place lo terminate avvakunda use cheyadaniki yield 
'''
def mygen():
    return "python"
    return "java"
    return "DSA"
print(mygen())
'''
'''
def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())
'''
#USING next()
'''
def mygen():
    yield "python"
    yield "java"
    yield "DSA"
d=mygen()
#print(*d)
print(next(d))
print(next(d))
print(next(d))
print(next(d))# we will get error here becoz the function have only 3 yield to display 
'''


        





