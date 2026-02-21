'''
#Run time Input

a=10
b=20
print(a+b)

a=10
b=20
c=a+b
print(c)

#With all DataTypes

a=int(input("Enter the Value:"))
b=int(input("Enter the Value:"))
print(a+b)

a=float(input("Enter the Value:"))
b=float(input("Enter the Value:"))
print(a+b)

a=str(input("Enter the Value:"))
b=str(input("Enter the Value:"))
print(a+b)

a=str(input("Enter the Value:"))
b=str(input("Enter the Value:"))
print(a+b)

a=bool(input("Enter the Value:"))
b=bool(input("Enter the Value:"))
print(a+b)

a=complex(input("Enter the Value:"))
b=complex(input("Enter the Value:"))
print(a+b)

#Example Code

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
option=int(input())
if option==1:
    print(a+b)

elif option==2:
    print(a-b)

elif option==3:
    print(a*b)

else:
    print(a/b)

   

#(SWAPPING)

a=10
b=20

a,b=b,a #method 1
print(a,b)

temp=a #method 2
a=b
b=temp
print(a,b)

a=a+b
b=a-b
a=a-b
print(a,b)

#Number Formatting
print("The values are a: %d,b: %d"%(a,b))    
print("The values are a: %f,b: %f"%(a,b))
print("The values are a: %.2f,b: %.3f"%(a,b))


