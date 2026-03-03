#range()

#start-stop-step
'''
for i in range(10):
    print(i)

for i in range(5,15):
    print(i)
'''

#TASK 1

'''
for i in range(0,50,5):
    print(i,end=" ")
print()  
for i in range(2,20,2):
    print(i,end=" ")
print()    
for i in range(3,30,3):
    print(i,end=" ")
'''

#TASK 2
'''
while True:
    marks=int(input("Enter the marks:"))
    if marks in range(91,101):
        print("GRADE A")
    elif marks in range(81,91):
        print("GRADE B")
    elif marks in range(71,81):
        print("GRADE C")
    elif marks in range(50,71):
        print("GRADE D")
    else:
        print("Fail")
'''

##Difference between break, continue and pass

#break is used to terminate the entir loop

#continue is used to skip the current iteration and rest of the code will continue

#pass is a null statement as it does nothing but syntactically we need.

#break
'''
a=10
while a<10:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break

a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)

for i in range(20):
    print(i)

for i in range(11):
    if i==11:
        break
    print(i)

'''
#continue
'''
a=30
while a>5:
    print(a)
    a=a=1
'''

'''
a=30
while a>5:
    a=a-1           
    print(a)
'''
'''
a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue
'''
'''
a=30
while a>5:
    if a==15:
        continue
    print(a)
    a=a-1
'''
'''
a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)
   
'''
#pass
'''
a=30
while a>20:
    print(a)
    a=a-1
'''
'''
a=30
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass
'''        
    












