 #List Comprehension

#Every List Comprehension can be rewritten as a for loop but every for loop cannot be rewritten in List Comprehension
'''
a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=" ")
print()
'''
#SYNTAX --> [expression     for     var     in       collection/range]
'''
b=[i.upper() for i in a]
print(b)

print([i.upper() for i in a])
'''

#TASK 1
'''
a=["python","java","Ml"]
print([i.capitalize() for i in a])
'''

#TASK 2
'''
a=[1,2,3,5,6,8,12,13]
b=[i*i for i in a]
print(b)
'''
'''
a=[1,2,3,5,6,8,12,13]
b=[i**2 for i in a]
print(b)
'''
'''#Using POWER--> pow()
a=[1,2,3,5,6,8,12,13]
b=[pow(i,2) for i in a]
print(b)
'''

#TASK 3 -- 'If' in list comprehension
'''
a=[i for i in range(16) if i%2==0]
print(a)
'''

#TASK 4
'''
a=[i*i for i in range(16) if i%2==0]
print(a)
'''

#TASK 5
'''
fruits=["apple","grapes","mang  o","banana","berry","kiwi","dragon","aei"]
a=[i for i in fruits if 'aei' in i]
print(a)
'''
#TASK 5.1
'''
inp=input()
if inp in 'AEIOUaeiou':
    print("Vowel")
'''

#TASK 6-- if else(DIFFERENT CASE)
'''
a=[i*i if i%2==0 else i*5 for i in range(21) ]
print(a)
'''

#TASK 7
'''#DONE BY ME
a=[1,2,3,4,5]
b=[5,4,3,2,1]

c=[i+j for i in a for j in b if i+j==6 ]   
print(c)
'''
 
'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)
'''

'''

