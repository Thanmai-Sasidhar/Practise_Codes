#Variable length arguments

#Variable length arguments are automatically stores in tuples and use * arguments
'''
def check(*a):
    print(a)
    print(type(a))                  
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(d)
e={3,4,5,6,7}
check(*e)
f={"name":"Sasi","city":"vja"}
check(*f)
'''

'''
def check(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i)==int or type(i)==float #Another--> type(i) in (int,float)                             :
            d+=i
            print(d)
check()
check(2,3,4,5,6,7)
check(2.3,4.5,5.5,6.5,4.2)
check(2.3,4.5,5.5,6.5,4.2,"SASI")
'''

#kwargs(**)
'''
def details(**a):
    print(a)
    print(type(a))
details()
d={"idno":[1,2,3,4,5],"names":["Sasi","Koushik","Aditya"],"status":["P","A","P"]}
details(**d)
'''
'''
def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    print()    
    for i in a.keys():
        print(i)
    print()
    for i in a:
        print(a[i])
    print()
    for i in a.values():
        print(i)
    print()
    for i in a:
        print(i,a[i])
    print()
    for i in a.items():
        print(i)
details()
d={"idno":[1,2,3,4,5],"names":["Sasi","Koushik","Aditya"],"status":["P","A","P"]}
details(**d)
'''

# * ,** usage
'''    
def final   (*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d+=i
        print(d)
    for i,j in b.items():
        print("Key is :",i)
        print("Values is :",j)
final()
data=(2,3,4,5.4,4.5,2.1)
final(*data)
details={"name":["Sasidhar","Koushik","Adithya"],"marks":[90,89,88]}
final(**details)
final(*data,**details)
'''

#max,min,sum
'''
print(max(4,5,6,12,20))
print(min(4,5,6,12,20))
print(sum([4,5,6,12,20]))#Without [] it generates error

a=2,3,4,5,5,6
print(sum(a))
'''

#Task
'''
n=int(input("Enter the No of Students: "))
a=0
arr=[]
for i in range(n):
    s=input(f"Enter the Student {i+1} Status: ")
    arr.append(s)
for i in arr:
    if i=="A":
        a+=1
p=n-a
print("Total No of Students:",n)
print("Presentees :",p)
print("Absentees :",a)
'''

n=int(input("Enter the No of Students: "))
a=0
p=0
arr=[]
for i in range(n):
    s=input(f"Enter the Student {i+1} Status: ")
    if s=="A":
        a+=1
    else:
        p+=1
print("Total No of Students:",n)
print("Presentees :",p)
print("Absentees :",a)




