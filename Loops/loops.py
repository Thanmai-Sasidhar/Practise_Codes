'''#Loops--> for ,while, range, break, continue, pass

#for() loop

#Using List

a=[10,20,30,40,50]
for i in a:
    print(i)

a=[10,20,30,40,50]
for i in a:
    print(a)

a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")

a=[10,20,30,40,50]
for i in a:
    print(a)
    print(type(a))
    print(type(i))

#Using Tuple 

a=(10,20,30,40,50)
for i in a:
    print(a)
    print(type(a))
    print(type(i))

#Using set

a={10,20,30,40,50}
for i in a:
    print(a)
    print(type(a))
    print(type(i))

#Using Dictionary

a={"name":"Sasi","year":2026,"month":3}
for i in a:
    print(i)

for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
    
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
    
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))

a="avanigadda"
for i in a:
    print(i)

a="avanigadda"
for i in a:
    print(i,end="")
    print(type(a))
    print(type(i))
'''


#Real time Example

#using for loop
'''
a=["code","python","course"]
for i in a:
    print(i.upper(),end="   ")
'''
#using slicing
'''
a=str(a)
a=a[:].upper()    

print(a)
'''
'''
#While Loop

a=10
while a>1:
    print(a)

a=20
while a>1:
    print(a)
    a=a-1

a=20
while a>=1:
    print(a)
    a=a-1

a=20
while a>1:
    print(a)
    a=a-1

a=20
while a>1:
    a=a-1
    print(a)

a=20
while a>1:
    a=a-1
print(a)

a=15
while a>2:
    print(a)
    a-=1

a=15
while a>2:
    print(a)
    a+=1

a=15
while a>=2:
    print(a)
    a-=1

a=3
while a<18:
    print(a)
    a*=1

a={10,20,30,40,50}
for i in a:
    print(i)

a={10,2,320,430,5}
for i in a:
    print(i)    

'''

#Voting using While
'''
while True:
    age=int(input("Enter the age "))
    if age>18:
        print("Eligible")
    elif age==-1:
        break
    else:
        print("Not Eligible")
'''        
                
        
