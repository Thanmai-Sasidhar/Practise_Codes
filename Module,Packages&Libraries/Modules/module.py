#MODULES PACKAGES AND LIBRARY

'''
# Difference bw module ,library and package
'''
#Modules
'''
1. Module in python is a single py file that contain python code

2. It typically consists of functions ,classes and variables that can be used in other python scripts or programs

3. Examples of modules includes math.py,random.py and mymodule.py

'''

#PACKAGE

'''
1.A package in python is a directory contaning one or more python modules  and an __init__.py file.

2. The __init__.py file can be empty or contain intilization code for package

3. Examples of packages numpy,pandas,django

'''

#Library
'''
1.Libraries consists of multiple modules and pacakges, organised to serve a particular purpose or domain

2.Examples of libraries such as requests, numpy, pandas and matplotlib

'''
#NOTE
'''
Every python file is a module and import is a keyword and every python file is saved internally
with varibale name as __main__

'''

"NOW GO AND CHECK MODULE_1.py"  


#math module

import math as m
'''
print(m.pi)
print(m.pi*3)
print(m.sqrt(2))
print(m.pow(2,2))
print(m.log(10))
print(m.ceil(2.123))
print(m.floor(1.2121))
print(m.sin(30))
print(m.cos(45))
print(m.tan(45))
'''
#Here the values are directly imported so we need not to call the pi with math

from math import pi,sqrt,log,pow,ceil,floor
print(pi)
