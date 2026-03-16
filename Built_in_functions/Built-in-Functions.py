#built-in functions

'''
#fromkeys()
a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"pooja")
print(b)'''


#eval():it will accept any datatype.
'''while True:
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    print(a+b)'''



'''while True:
    a=float(input("enter the value of a"))
    b=float(input("enter the value of b"))
    print(a+b)'''



'''while True:
    a=(input("enter the value of a"))
    b=(input("enter the value of b"))
    print(a+b)'''



'''while True:
    a=eval(input("enter the value of a"))
    b=eval(input("enter the value of b"))
    print(a+b)'''


#zip():we can combine multiple collection in to one collection
'''a=[10,20,30,40,50]
names=["ad","it","ya","na","gen"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''


'''
#enumerate():we can give counter to the collection

names:["adi","tya","nag","end","ra"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names,100))
print(b)

b=list(enumerate(names,100))
print(b)

b=set(enumerate(names,100))
print(b)

b=tuple(enumerate(names,100))
print(b)'''



#tasks on ascii value

'''
print(a to z)
print(A to Z)
print(Ascii for my name)
'''

