#Multi-level inheritance
'''
class Dog_breed1():
    def f1(self):
        print("Breed 1 eats f1")
class Dog_breed2(Dog_breed1):
    def f2(self):
        print("Breed 2 eats f2")
class Dog_breed3(Dog_breed2):
    def f3(self):
        print("Breed 3 eats f3")
a = Dog_breed3()
a.f3()
a.f2()
a.f1()
'''
#super() 

'''
The super function is used to give access to methods and properties of a parent or sibling class

The super function returns an object that represents the parent class

In python super() is used to call methods from a parent (super class) inside a child(sub class) it allows to
extend or override inherited methods while still re using the parents functions
'''

#Example program for super()
'''
class parent():
    def __init__(self,name):
        self.name=name
        print("parent class connstructor")

class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child class constructor")

c=child("Sasidhar",26)
print(c.name,c.age)
'''

#ENCAPSULATION
'''
Combine multiple units into singlen unit is called encapsulation

In this we have 3 step

1.Public Data

2.Protected Data _

3.Private Data __

'''

#PUBLIC DATA
'''
class parent():
    public_data=26 # Gobal varibae 
    def method_1(self):
        print(self.public_data)
class child(parent):
    def method_2(self):
        print("")
obj=child()
obj.method_1()
obj.method_2()
'''
#CONTACT BASED MANAGEMENT SYSTEM
'''
1.Add
2.Update
3.List of contacts
4.Delete
5.Exit


Name,mobile,mail id

Five classes for all the transactions

'''






