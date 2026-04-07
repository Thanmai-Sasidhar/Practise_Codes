# Encapsulation 

#Encapsulation :-
'''
Combine multiple units into single unit is called encapsulation
1.Public data 
2.Protected data  _ (single underscore)
3.Private data  __ (Double underscore)
'''

#Public data :-
'''
class parent():
    publicdata=10
    def method1(self):
        print(self.publicdata)

class child(parent):
    def method2(self):
        print(self.publicdata)
obj=child()
obj.method1()
obj.method2()
'''

#_Protected data :-
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
print(obj1._protecteddata)'''


#__privatedata()
'''
class parent():
    __privatedata=100
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):

    
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()
'''


#Abstraction

#abstraction:-the process of handling complexity by hiding unnessesary info from user is called abstraction.
#abstract class: if a class contain one or more than one abstract method then the class is called abstract class.
#abstract method: is the method is decleared without implementation is called abstract method.

'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''


'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''    #error

#actual code:
'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("menthod3 is implemented")
obj1=B()
obj1.method1()
obj2.method2()
obj3.method3()'''      








