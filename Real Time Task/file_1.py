VOTING
'''
age=int(input("Enter the age:"))
if age>=18::
    print("Eligible")
else:
    print("Not Eligible")
'''
EVEN OR ODD
'''
n=int(input("Enter the Number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")
'''
LEAP YEAR
'''
year=int(input("Enter the Year:"))
if (year%4==0 and year%100==0) or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
'''
VOWELS
'''
v=input("Enter the Letter:")
if v in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")
'''
Name printing
'''
name=input("Enter any name:")

if name=="Sasi":
    print("Welcome Sasi")
else:
    print("Welcome Guest")
'''
Name printing of 5 names
'''
names=["Thanmai","Sasidhar","Avani","Dhanu","Jalaja"]    
name=input()
if name in names:
    print("Welcome",name)
else:
    print("Welcome Guest")
'''
Name printing by Dynamic input
'''
names=list(map(str,input().split()))    
name=input()
if name in names:
    print("Welcome",name)
else:
    print("Welcome Guest")
'''    
Social Media Login
'''
username=input()
password=int(input())

if username=="Sasi":
    if password==1234:
        print("Login Successful")
    else:
        print("Invalid Credentials")
else:
    print("Invalid Credentials")
'''
Social Media using if-else
'''   
username=input()
password=input()

if username=="Sasi" and password=="abc":
    print("Login Successfully")

else:
    print("Invalid Credentials")
'''
Bakery Cakes And prices
'''
price=int(input())

if price==1200:
    print("Red Velvet Cake")
elif price==1000:
    print("Chocolate Cake")
elif price==800:
    print("Butterscotch Cake")
elif price==600:
    print("Choco-Almond Cake")
else:
    print("Sorry Cake is not available")
'''

Using Dictionary extracting values using keys
'''
cakes={"a":1000,"b":2000}
cake=input()

if cakes.get(cake):
    print(cakes[cake])
else:
    print("Invalid Key")
'''    

