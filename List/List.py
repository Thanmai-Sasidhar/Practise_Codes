Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#List

#append
a=[1,2.3,"4",True,False,2j+6]
type(a)
<class 'list'>
a.append("hi")
a
[1, 2.3, '4', True, False, (6+2j), 'hi']
a.append([1,2,3,4])
print(a)
[1, 2.3, '4', True, False, (6+2j), 'hi', [1, 2, 3, 4]]
a.pop()
[1, 2, 3, 4]
a.pop(3)
True
a
[1, 2.3, '4', False, (6+2j), 'hi']
a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)

#extend

a.extend(["hello","world"])
a
[1, 2.3, '4', False, (6+2j), 'hi', 'hello', 'world']
#Here in both the cases we have to given inside the [] only but whats the difference is seen in the output
a.extend("hello","world")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.extend("hello","world")
TypeError: list.extend() takes exactly one argument (2 given)

#insert()

a=["APPLE","BANANA","KIWI"]
a.insert(0,"Mango")
a
['Mango', 'APPLE', 'BANANA', 'KIWI']
#a.insert(position number,Argument)--->Syntax

a=["zero","one","two","three","four"]
b=a
b
['zero', 'one', 'two', 'three', 'four']

a.index("one")
1
a.index("three")
3
b=a.copy()
b
['zero', 'one', 'two', 'three', 'four']
b=a.copy()
b
['zero', 'one', 'two', 'three', 'four']

a=["z","s","f","a","t"]
a.sort()
a
['a', 'f', 's', 't', 'z']
a=[9,8,7,6,5,4,3,2,1]
a.sort()
a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
a=["1","a","123"]
a.sort()
a
['1', '123', 'a']
a=[1,"a"].sort()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a=[1,"a"].sort()
TypeError: '<' not supported between instances of 'str' and 'int'
a=[1,2.3,0.4]
a.sort()
a
[0.4, 1, 2.3]
a=[1,2,3,4,5,6,7,8,9]
a.reverse()
a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
b=["Hi","Hello","Good Morning"]
print(b.reverse())
None
b.reverse()
b
['Hi', 'Hello', 'Good Morning']
b.reverse()
b
['Good Morning', 'Hello', 'Hi']
b.pop()
'Hi'
b.pop("Hello")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    b.pop("Hello")
TypeError: 'str' object cannot be interpreted as an integer
b.pop(0)
'Good Morning'
b
['Hello']
a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
(a.sort()).reverse()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    (a.sort()).reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
a.sort().reverse()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.sort().reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
a.sort()
a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#remove

a=["hi","hello","How"]
a.remove("hi") #Here it is different from pop as that takes only index value but here the remove takes the Argument
a
['hello', 'How']
b=sorted(a,reverse=True)
a
['hello', 'How']
b
['hello', 'How']

a=["code"]
len(a)
1
a="code"
len(a)
4
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
b=sorted(a,reverse=True)
b
[9, 8, 7, 6, 5, 4, 3, 2, 1]


#count()

a=["Sun","Moon","Earth","Sun"]
a.count("Sun")
2
a.count(Earth)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.count(Earth)
NameError: name 'Earth' is not defined
a.count("Earth")
1
a.count("a")
0
str(a)
"['Sun', 'Moon', 'Earth', 'Sun']"
a.count(u)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.count(u)
NameError: name 'u' is not defined

a.count("u")
0
#clear()
A
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
['Sun', 'Moon', 'Earth', 'Sun']
a.clear()
a
[]
a=["Sun","Moon","Earth","Sun"]


a=[9,1,5,2,8,4,6,3,7,0] #[7,6,4,3,0,9,8,5,2,1]
a.replace(7,9)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.replace(7,9)
AttributeError: 'list' object has no attribute 'replace'
>>> b=[9,1,5,2,8]
>>> c=[4,6,3,7,0]
>>> b.sort()
>>> b
[1, 2, 5, 8, 9]
>>> b.reverse()
>>> 
>>> b
[9, 8, 5, 2, 1]
>>> c
[4, 6, 3, 7, 0]
>>> c.sort()
>>> c
[0, 3, 4, 6, 7]
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> b+c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> c=B
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    c=B
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> c+b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
>>> #tuple()
>>> 
>>> a=(1,2.3,"4")
>>> type(a)
<class 'tuple'>
>>> a.index("4")
2
>>> a.count(1)
1
>>> len(a)
3
>>> 
>>> #Tuple is immutable data type as we cannot chnage anything in it after assigning values 
