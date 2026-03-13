#File Handling

#write()
'''
a=open("sasi.txt","w")
a.write("Thanmai Sasidhar")
a.close()
 
a=open("sasi.txt","w")
a.write("Python")
a.close()
'''
#append()
'''
a=open("sasi.txt","a")
a.write("\t Avanigadda")
a.close()
'''
#run_time input()
'''    
a=open("sasi.txt","w")
a.write(input("Enter the Data:"))
a.close()

a=open("sasi.txt","w")
b=input()
a.write(b)
a.close()

a=open("sasi.txt","w")
b=input("Enter the Data :")
a.write(b)
a.close()
'''

#readlines

'''
a=open("sasi.txt")
'''
#reading whole file contect
'''
print(a.read())
'''
#Reading first line of the content
'''
print(a.readline())
'''
#Reading all lines
'''
print(a.readlines())
'''
#Reading lines upto specific no of characters
'''
print(a.read(7))
'''

#writelines()
'''
a=open("data.txt","w")
b=["python","java","html","css","DSA"]
a.writelines("\n".join(b)) #Using Join to use \n
a.close()

a=open("sasi.py")
print(a.read())
'''
#Cannot open other directory files as only open the file with in the directory


#For paths we must use // instead of /
'''
a=open("//Users//ats//Desktop//Python_CG\ copy//    Day\ 1.py")
print(a.read())
'''

#ERROR HANDLING

#There are 3 types of Error Handling -->1.Run Time 2.Compile Time 3.Logical Error

#Syntax Error
'''
for i in range(10)
    print(i)
'''
#Run Time Error
'''
a=int(input())
b=int(input())
print(a//b)
'''
'''
OUTPUT:
5
0
Traceback (most recent call last):
  File "/Users/ats/Desktop/Python_CG/File_handling.py", line 89, in <module>
    print(a//b)
ZeroDivisionError: integer division or modulo by zero
'''

#Logical Error

#Without error
'''
a=5
b=2
if a>b:
    print("true")
'''
#With error
'''
a=5
b=2
if a<b:
    print("true") #As it does not prints anything as it is a logical error 
'''    

#-------------------------------------------Exception Handling--------------------------------------------------

'''

try block ---> Instrctions from which we are expecting the exceptions

except --> Exception raised in try block will be handled in this block

else ---> It is optional and No exception,As it works when try blocks executes correctly 

finally ---> Always it will display

'''

#Exception Handling
while True:
    a=int(input())
    b=int(input())
    try:
        c=a//b
        print(c)
    except:
        print("Exception is raised")
    else:
        print("No Exceptions")
    finally:
        print("Program End...")


    
