Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#integer --> 1,12,123
#float --> 1.0,12.3
#boolean -->True , False
#string --> "Hello"
#complex --> 1+2j



a=100
type(a)
<class 'int'>
c=8.9
type(c)
<class 'float'>
b='Hi'
type(b)
<class 'str'>
d="Python"
type(d)
<class 'str'>
g="True"
type(g)
<class 'str'>
g=True
type(g)
<class 'bool'>
e=2i+3
SyntaxError: invalid decimal literal
e=2+3i
SyntaxError: invalid decimal literal
e=2j+3
type(e)
<class 'complex'>



#DataType Conversions


================================ RESTART: Shell ================================
#DataType Conversions


int(7)
7
int(7.6)
7
#In integer string and complex cannot be converted
int("Hello")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int("Hello")
ValueError: invalid literal for int() with base 10: 'Hello'
int(1+2j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(1+2j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1

#Float

float(1)
1.0
float(2.0)
2.0
float(True)
1.0
float("Hi")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    float("Hi")
ValueError: could not convert string to float: 'Hi'
float(1+2j)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(1+2j)
TypeError: float() argument must be a string or a real number, not 'complex'


#String

str(7)
'7'
str(1.2)
'1.2'
str("Hello")
'Hello'
>>> str(True)
'True'
>>> str(1+2j)
'(1+2j)'
>>> 
>>> 
>>> #Complex
>>> 
>>> complex(2)
(2+0j)
>>> complex(2.0)
(2+0j)
>>> complex("Hello")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex("Hello")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(1+2j)
(1+2j)
>>> 
>>> 
>>> #Boolean
>>> 
>>> bool(1)
True
>>> bool(5)
True
>>> bool(3.2)
True
>>> bool("Hello")
True
>>> bool(True)
True
>>> bool(1+2j)
True
