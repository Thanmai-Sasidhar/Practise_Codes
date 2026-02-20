Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={3,5.5,"simhadr",5+6j,True,False}
print(a)
{False, True, 3, 5.5, (5+6j), 'simhadr'}
type(a)
<class 'set'>
b={7,5,6,7,8,6,5}
print(b)
{8, 5, 6, 7}
type(b)
<class 'set'>
#setmethods
#add
a={3,4,5,2,7,8}
a.add(10)
a
{2, 3, 4, 5, 7, 8, 10}
#subset
a={3,4,5,6,7}
b={5,6}
a.issubset(b)
False
b.issubset(a)
True
a={3,4,5}
b={1,2,6}
a.issubset(b)
False
b.issubset(a)
False
a={3,4,5,6,7,8,9}
b={4,5,6}
a.issuperset(b)
True
b.issuperset(a)
False
a={"s","i","m","h","a"}
b={"s","h"}
a.issuperset(b)
True
b.issuperset(a)
False
#Union()
a={3,4,5,6,7,8}
b={2,3,4,5,9}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9}
#intersection
a=4,5,6,7,8,9
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#printing same values in sets

##difference
a{2,3,4,5,6}
SyntaxError: invalid syntax
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}
b.difference(a)
{8, 7}
#value which are not in another set that prints as output

#update
a={10,11,12,13,14}
b={11,12,13,14,15}
a.update(b)
a
{10, 11, 12, 13, 14, 15}
b.update(a)
b
{10, 11, 12, 13, 14, 15}

a={4,5,6,7,8,9}
b={2,3,4,5,6,7,8,9,10}
a
{4, 5, 6, 7, 8, 9}
a.difference_updateb(b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.difference_updateb(b)
AttributeError: 'set' object has no attribute 'difference_updateb'. Did you mean: 'difference_update'?
a.difference_update(b)
a
set()
a={2,3,4,5,6,7}
b={1,5,7,9,11,12}
a.difference_update(b)
a
{2, 3, 4, 6}
b.difference_update(a)
b
{1, 5, 7, 9, 11, 12}
#By this method first we can find difference and after update the value of that set


#symmetric difference
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}


#symmetric update
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'

#symmetric_difference_update
a={1,3,4,7,9,11,13}
b={2,3,4,6,8,10,12}
a.symmetric_differece_update(b)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.symmetric_differece_update(b)
AttributeError: 'set' object has no attribute 'symmetric_differece_update'. Did you mean: 'symmetric_difference_update'?
a.symmetric_difference_update(b)
a
{1, 2, 6, 7, 8, 9, 10, 11, 12, 13}
b.symmetric_difference_update
<built-in method symmetric_difference_update of set object at 0x0000023C5ED21700>
b.symmetric_difference_update(a)
b
{1, 3, 4, 7, 9, 11, 13}

#intersection_update
a={7,8,9,7}
b={2,3,4,5,6,7,8,9}
a.intersection(b)
{8, 9, 7}
b.intersection(a)
{8, 9, 7}


a={5,6,7,8,9,10}
a.pop()
5
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a.remove(10)
a
{6, 7, 8, 9}

#copy
a={3,4,5,6,7}
a.copy()
{3, 4, 5, 6, 7}
>>> a.clear()
>>> a
>>> 
>>> a.clear()
>>> 
>>> #clear
>>> a={3,4,5,6,7}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(56)
>>> b
{56}
>>> #discard
>>> a={3,4,5,6,7,8}
>>> b={2,4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a={7,8,9}
>>> b={2,3,4}
>>> a.isdisjoint(b)
True
>>> #Both sets are having different values or opposite values
>>> 
>>> a={5,6,7,8}
>>> len(a)
4
>>> a.count(2)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a.count(2)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
