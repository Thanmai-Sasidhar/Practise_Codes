#Keyword and positional arguements

'''def details(id,name,mailid):
    id=10
    name="simhadri"
    mailid="simha@mail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''


'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="chandana",mailid="c@gmail.com")
details(id=40,name="jyoshnavi",mailid="j@gmail.com")
details(id=60,name="harika",mailid="h@gmail.com")
details(80,"taruni","t@gmail.com")
details(id=100,name="simhadri",mailid="s@gmail.com")
details("id","name","mailid")'''

#Default arguements

'''def grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("sugar",100)'''

'''def grocery(item="rice",price=1333):
    print("item is %s"%item)
    print("price is %d"%price)
grocery()'''

'''def grocery(item,price=1333):
    print("item is %s"%item)
    print("price is %d"%price)
grocery("dhal")'''

'''def grocery(item="rice",price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery(1333)'''

#Task
'''def bakery(item,price,quantity):
    print("item is %s" %item)
    print("name is %d" %price)
    print("quantity is %s" %quantity)
bakery("chocolate",1300,"4kg")'''

'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(2,3,4,5,6,7,8)
print(b)
print(*b)'''

'''c={2,3,4,5,6,7,8)
print(c)
print(*c)
(type(c))'''

'''d={"year":2026,"month":3}]
print(d)
print(*d)
(type(d))'''

'''a,b,c=2,3,4,5,6,7,8
print(a)
print(b)
print(c)'''#error


'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8
print(a)
print(*b)
print(c)'''


'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

