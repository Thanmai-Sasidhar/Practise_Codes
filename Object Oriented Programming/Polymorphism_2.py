#polymorphism:
#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(6))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__le__(8))
print(a.__ge__(3))
a=[1,2,3,4,5,6,7];b=[6,7,8,9,10,11]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(5))
a="code";b="gnan"
print(a.__add__(" "+b))
print("pooja".__add__(" "+"ch"))
print("adithya"._add_(" "+"python").title())'''


#operator overriding:
''' class A():
     def __init__(self,a):
         self.a=a
     def __add__(self,value):
         return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
print(x+y)
#x=6
#y=4
#print(x+y)'''


#method overloading:
'''class New():
     def sum(self,a=2,b=4,c=6):
        if a!=None and b!=None and c!=None:
             print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("Program ends")
x=New()
x.sum()'''

#task
'''class New():
     def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
             print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("Program ends")
x=New()
x.sum()'''

'''class New():
    def sum(self, a=2, b=4, c=6):
        if a==2 and b==4 and c==6:
            print("the sum is", a+b+c)
        elif a==2 and b==4:
            print("the product is", a*b)
        else:
            print("Program ends")

x=New()        
x.sum(2,4,6)   
x.sum(2,4,0)   
x.sum(1,2,3)'''



#method overriding:
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


#task
'''
class HybridBike():
    def speak(self):
        print("Loud sounds")
class ElectricalBike():
    def speak(self):
        print("less sounds")
a=HybridBike()
b=ElectricalBike()
a.speak()
b.speak()
'''
