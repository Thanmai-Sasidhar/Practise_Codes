#Difference bw _ and __

'''
We genarally use '__' for private variables that means whenever we use ___ underscore for a varibale our python
interpreter treats it as a special variable in order to avoid name conflicts with methods in inner classes
'''

#Example
'''
class Employee():
    def __init__(self):
        self.name="SASI"
        self._mail="ats@gmail.com"
        self.__salary=100000

a=Employee()
print(dir(a))
print(a.name)
print(a._mail)
#print(a.__salary) # As it is a private varible it does gives output as it raises error

print(a._Employee__salary) #IMPORTANT as it displays private variable's data
'''

#TASK
'''
class Employee():
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary

a=Employee("sasi","ats.com",100000)
b=Employee("Thanmai","Sasi.com",20000)
print(a.name)
print(a._mail)
print(a._Employee__salary)

print(b.name)
print(b._mail)
print(b._Employee__salary)

'''

#POLYMORPHISM

#OPERATOR OVERLOADING
'''
Based on the input or variables the operation performance will be changed like as + as SUM ,CONCAT, MERGE
'''
#USING NUMBER AS INPUT
'''
a=2;b=5
print(a+b)

print(a.__add__(b))

print(a.__sub__(b))

print(a.__mul__(b))

#print(a.__div__(b)) # As __div__ is not present in the module of python 

print(a.__le__(b))

print(a.__ge__(b))
'''

#USING LIST AS INPUT
'''
a=[1,2,3,4,5];b=[6,7,8,9,10]

print(a.__add__(b))

print(a.__getitem__(1))

print(b.__getitem__(1))

a="thanmai";b="sasidhar"

print(a.__add__(b))

print(a.__add__(" "+b))

print((a.__add__(" "+b)).title())

print((a.title()).__add__(" "+b.title()))
'''




