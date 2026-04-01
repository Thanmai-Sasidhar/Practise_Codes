#System module
'''
import sys
print(sys.path)

for i in sys.path:
    print(i)
'''
#OS module

#It is used when we need to know the loaction of a file in the project 
'''
import os

print(os.path)

print(os.chdir("/Users/ats/Desktop/Python_CG_copy"))

print(os.getcwd())

print(os.listdir())
    
print(os.mkdir("ATS"))
'''

#random module

'''
To generate random number in python , randint function is used this function is defined in random module

Python defines a set of functions that are used to generate or manipulate random numbers through the
random module

'''
#sample()
'''
import random
a=random.sample(range(10,20),5)
print(a)
'''
#randint()
'''
import random
a=random.randint(40,60)
print(a)
''' 
#choice()
'''
import random
a=[1,2,3,4,5,6]
b=random.choice(a)
print(b)
'''

#TASK (LUDO DICE NUMBER GENERATOR)
'''
import random
while True:
    n=int(input("Enter the roll of dice : "))
    b=random.randint(1,6)
    print(b)
    opt=int(input("1.Yes \n2.No"))
    if opt==1:
        continue
    else:
        print("Exit")
        break
'''

#Calender module
'''
import calendar as c

year=2026
month=4
print(c.month(year,month))
'''

'''
import calendar as c
year=2027
print(c.calendar(year))
'''
'''
import calendar as c

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
print(c.month(year,month))  
'''


                    





    
    

