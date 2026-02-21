Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={"Name":"Sasidhar","Phno":"12345678"}
>>> a.get("name")
>>> a.get("Name")
'Sasidhar'
>>> a.clear()
>>> a
{}
>>> a.update("Name:SASI")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update("Name:SASI")
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a.update({"Name:SASI"})
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.update({"Name:SASI"})
ValueError: dictionary update sequence element #0 has length 9; 2 is required
>>> a.update{"Name:SASI"}
SyntaxError: invalid syntax
>>> a={"Name":"Sasidhar","Phno":"12345678"}
>>> a.update({"Gender":"Male"})
>>> a
{'Name': 'Sasidhar', 'Phno': '12345678', 'Gender': 'Male'}
>>> 
>>> a.clear()
>>> a={"IdNo:":[1,2,3,4],"Names":["ATS","DNS","KJK","ABR"],"Places":["Kanuru","Chennai","Vijayawada","Nuzvid"]}
>>> a.keys()
dict_keys(['IdNo:', 'Names', 'Places'])
>>> a.values()
dict_values([[1, 2, 3, 4], ['ATS', 'DNS', 'KJK', 'ABR'], ['Kanuru', 'Chennai', 'Vijayawada', 'Nuzvid']])
>>> a.items()
dict_items([('IdNo:', [1, 2, 3, 4]), ('Names', ['ATS', 'DNS', 'KJK', 'ABR']), ('Places', ['Kanuru', 'Chennai', 'Vijayawada', 'Nuzvid'])])  
