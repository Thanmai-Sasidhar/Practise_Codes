Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Operators
>>> 
>>> #Arithmetic --> +,-*,/,//,**,%
>>> #Assignment --> +=,-=,*=,//=,/=,**=,%=
>>> #Comparison --> >,<,>=,<=,!=,==
>>> #Logical --> and, or, not
>>> #Identify --> is ,is not
>>> #Membership --> in ,not in
>>> #Bitwise --> &, ||, !, >>, <<
>>> 
>>> #Arithmetic
>>> 
>>> a,b=1,2
>>> print(a+b,a-b,a*b,a/b,a//b,a**b,a%b)
3 -1 2 0.5 0 1 1
>>> 
>>> #Assignment
>>> 
>>> a,b=4,6
>>> 
>>> a+=b
>>> a
10
>>> a-=b
>>> a
4
>>> a/=b
>>> a
0.6666666666666666
>>> a*=b
>>> a
4.0
>>> a%=b
>>> a
4.0
>>> a//=b
>>> a
0.0
>>> b
6
>>> b**=a

b
1.0
c=6
b+=c
b
7.0
b-=c
b
1.0


#Comparison

a>b
False
a<b
True
a!=b
True
a==b
False
a>=b
False
a<=b
True

print(a,b)
0.0 1.0

#Logical

a,b=6,12

a<b and b>a
True
a!=b and a==a
True
a<=b or b<=a
True
a>=b or b>=a
True
not True
False
not False
True


#Identity

a,b=4,4.5

if type(a) is int:
    print("Integer")

    
Integer
if type(b) is not int:
    print("False")

    
False
if a==b:
    print("Equal")
else:
    print("Not Equal")

    
Not Equal


#Membership

a=[1,2,3,4]
if 2 not in a:
    print(False)
else:
    print(True)

    
True

#Bitwise Operator

a=8
a<<2
32
a<<1
16
a>>1
4
a&b
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a&b
TypeError: unsupported operand type(s) for &: 'int' and 'float'
a,b=8,16
a&b
0
a||b
SyntaxError: invalid syntax
a|b
24
a!b
SyntaxError: invalid syntax
a~b
SyntaxError: invalid syntax
~b
-17
a,b=7,8
a|b
15
a=4
a<<3
32
a=6
a<<2
24
a=8
a>>2
2
