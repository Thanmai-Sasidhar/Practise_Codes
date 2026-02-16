Python 3.14.0 (tags/v3.14.0) on win32
Enter "help" below or click "Help" above for more information.

#Indexing
>>> a="Knowledge is power"
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
'Knowledge'
>>> a[9]
' '
>>> a[10]+a[11]
'is'
>>> a[12]
' '
>>> a[13]+a[14]+a[15]+a[16]+a[17]
'power'

>>> a[10]+a[11]+a[10]+a[11]
'isis'

>>> a="Coding is fun"
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Coding'
>>> a[6]
' '
>>> a[7]+a[8]
'is'
>>> a[9]
' '
>>> a[10]+a[11]+a[12]
'fun'


# Negative indexing
>>> a="Practice daily"
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]
'yliad'
>>> a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'daily'
>>> a[-6]
' '
>>> a[-11]+a[-10]+a[-9]+a[-8]+a[-7]
'Pract'
>>> a[-12]+a[-11]+a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'Practic'
>>> a[-13]+a[-12]+a[-11]+a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'Practice'

>>> a="Stay focused"
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'focused'
>>> a[-8]
' '
>>> a[-12]+a[-11]+a[-10]+a[-9]
'Stay'
