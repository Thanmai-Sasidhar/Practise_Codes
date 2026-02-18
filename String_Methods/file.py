Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String Methods

a="Codegnan"
len(a) #length
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

# count()--> method

a="Twinkle Twinkle little star"
a.count("Twinkle")
2
a.count("twinkle")
0
a.count("e")
3
a.count(" ")
3

#Find a string
a="Thanmai"
a.find("T")
0
a.find("a")  #Gives the first occuring index value only
2

a.find("q")
-1

#Escape Sequences

a="Hi\nMy name is Thanmai Sasidhar Avanigadda\nPhno:7989278659\nKanuru\tVijayawada"
a
'Hi\nMy name is Thanmai Sasidhar Avanigadda\nPhno:7989278659\nKanuru\tVijayawada'
print(a)
Hi
My name is Thanmai Sasidhar Avanigadda
Phno:7989278659
Kanuru	Vijayawada


#replace()

a="wait wait until you succeed"
a.replace("wait","work")
'work work until you succeed'
a
'wait wait until you succeed'
a.replace("wait","work",1)
'work wait until you succeed'
'work wait until you succeed'
'work wait until you succeed'
a.replace("ai","AI")
'wAIt wAIt until you succeed'

#Uppercase -->upper()
a="hello world"

a.upper()
'HELLO WORLD'
a.capitalize()
'Hello world'
a.title()
'Hello World'
a.lower()
'hello world'

a="I am in HYD"
a.capitalize()
'I am in hyd'
a.title()
'I Am In Hyd'
a.upper()
'I AM IN HYD'
a.lower()
'i am in hyd'

#isupper, islower, isdigit, startswith, isalpha, isalnum

a="THANMAI"
a.isupper()
True
b="hi"
b.islower()
True
c="26"
c.isdigit()
True
c=26
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a.isalnum()
True
a.startswith("T")
True
a.startswith("Th")
False
a.endswith("I")
True
a="Hi26"
a.isalpha()
False
a.isalnum()
True

#strip()
a="     Hello World     "
a.strip()
'Hello World'
a.lstrip()
'Hello World     '
a.rstrip()
'     Hello World'
#split()

a="Hi, my name is Thanmai Sasidar"
a.split()
['Hi,', 'my', 'name', 'is', 'Thanmai', 'Sasidar']
a.split(",")
['Hi', ' my name is Thanmai Sasidar']

#join()
a="hi","Everyone","Good Morning"
"".join(a)
'hiEveryoneGood Morning'
" ".join(a)
'hi Everyone Good Morning'
",".join(a)
'hi,Everyone,Good Morning'

#concatenation ---> +

a="code"
b="hunt"
print(a+b)
codehunt
print(a+" "+b)
code hunt
print(a+" "+b).title()
code hunt
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(a+" "+b).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((a+" "+b).title())
Code Hunt
print((a+" "+b).capitalize())
Code hunt

#formatting

a,b=1,1
print("The Sum is",a+b)
The Sum is 2

a,b="Thanmai","Avanigadda"
print("The full name is",(a+" "+b))
The full name is Thanmai Avanigadda
print("The full name is",(a+" "+b).lower())
The full name is thanmai avanigadda
print("The full name is",(a+" "+b).upper())
The full name is THANMAI AVANIGADDA
The full name is THANMAI AVANIGADDA
SyntaxError: invalid syntax


print("The full name is",(a+" "+b).title())
The full name is Thanmai Avanigadda




#format method
a="motu"
b="patlu"
print("Hello,"(a+" "+b))
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print("Hello,"(a+" "+b))
TypeError: 'str' object is not callable
print("Hello,",(a+" "+b))
Hello, motu patlu
print("Hello, {} {}".format(a,b))
Hello, motu patlu
print("Hello, {},{}".format(a,b))
Hello, motu,patlu
print(("Hello, {} {}".format(a,b)).title())
Hello, Motu Patlu

a="John"
b="Henry"

print(f"Hello {a},{b}")
Hello John,Henry
print(f"Hello {a},{b}".title())
Hello John,Henry
#fstring
