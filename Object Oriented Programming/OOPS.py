#OOPS (Object Oriented Programming)

'''
1.A class contains attributes (or) varibales and methods (or) functions that can manipulate the data

2.A class is the blueprint of an object.

3.An is an intiation of a class.

4.Methods or functions define inside the body of the class.

'''

#Syntax of OOPS
'''
class classname():
    name="CG"
    age=20
    place="VJA"
    def fname(method):     # Generally we take 'self' as a method
        print("STATEMENT...")
a=classname()
print(dir(a))
a.fname()
'''
#Class Declaration
'''
class Details():
    name="Sasidhar"     #
    age=20              #  This is used to add the variables to directory 
    place="Vijayawada"  #

    def display(self):
        print(self.name,self.age,self.place) 
a=Details()
print(dir(a)) #prints the modules inside the class
a.display()
'''
#Object instatiation or creation
'''
class Details():
    def Data(self,name,age,place):       #Appudina Function rase appudu conform ga method(self) undali and next attribute undali 
        self.name=name                   #Attributes ki conform ga method undali so manam ekkada self.name ani use chestam instead of name=name
        self.age=age
        self.place=place
    def display(self):                       #Function for declaration
        print(self.name,self.age,self.place)
a=Details()  #Here it is the object as it is calling outside the class
print(dir(a))# Here the modules will not be added to the directory as we does not given any values
a.Data("Sasi",20,"Vijayawada")
a.display()

b=Details()
b.Data("Dhanushya",24,"Chennai")
b.display()        
'''

#Object Initialisation
'''
class details():
    #Creating Constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
#The main difference bw normal declaration and init is
        #init lo direct ga values pass cheyochu with the class name but
            #normal method after object creation ,method name tho call cheyali 
a=details("Sasi",23,"Vja")
a.display()
'''

#Task ---> RUNTIME

#Method 1
'''
class details():
    def __init__(self):#Here you have to remove name,age,place as we are taking the input in run time   
        self.name=input("Enter ur name:")
        self.age=int(input("Enter Age: "))
        self.place=input("Enter Place: ")
    def display(self):
        print(self.name,self.age,self.place)
a=details()
a.display()
'''
#Method 2
'''
class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name=input("Enter ur name: ")
age=int(input("Enter Age: "))
place=input("Enter Place: ")
a=details(name,age,place)
a.display()
'''
#Method 3
'''
class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=details(input("Enter the name: "),int(input("Enter the age: ")),input("Enter the place: ")) #Taking the input inline
a.display()
'''


