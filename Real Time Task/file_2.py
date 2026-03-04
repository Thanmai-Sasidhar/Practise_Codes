# Printing the multiplication table
'''
n=int(input("Enter the integer: "))

for i in range(1,21):
    print(n,"x",i,"=",n*i)
'''
# Student Profile
'''
name=input("Enter the Name of the Student:")
mobile=int(input("Enter the Number of the Student:"))
mail=input("Enter the E-mail of the Student:")          
college=input("Enter the College Name:")
Branch=input("Enter the branch:")
print("**********STUDENT PROFILE**********")
print("Name:",name,"\nMobile No:",mobile,"\nMail:",mail,"\nCollege Name:",college,"\nBranch:",Branch)
'''
#Marks Analyser
'''
n=int(input())
arr=[]

for i in range(n):
    m=int(input(f"Enter the Marks of Student {i+1}: "))
    arr.append(m)        

total=sum(arr)
avg=total/n
arr.sort()
print("*******STUDENT REPORT*******")
print("Highest Mark:",arr[-1])
print("Lowest Marks:",arr[0])
print("Total Marks:",total)
print("Average:",avg)
'''
#Using max and min
'''
n=int(input())
arr=[]

for i in range(n):
    m=int(input(f"Enter the Marks of Student {i+1}: "))
    arr.append(m)        

maxi=max(arr)
mini=min(arr)
total=sum(arr)
avg=total/n

print("*******MARKS  REPORT*******")
print("Highest Mark:",maxi)
print("Lowest Marks:",mini)
print("Total Marks:",total)
print("Average:",avg)
'''

#Hostel fee and Course Fee
h=int(input("Enter Hostel fee: "))
c=int(input("Enter Course Fee: "))
print("**********SUMMARY**********")
print("The Hostel Fee is :",h)
print("The Course Fee is :",c)
print("Total Fee is:",h+c)

#Pattern
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()    
 
    
