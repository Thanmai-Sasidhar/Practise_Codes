Python 3.13.0 (v3.13.0:60403a5409f, Oct 7 2024, 00:37:40)
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

>>> s = "CodeGnan"
>>> s[0:3]
'Cod'
>>> s[0:4]
'Code'
>>> s[4:8]
'Gnan'
>>> s[4:]
'Gnan'
>>> s[0] + s[1] + s[1] + s[2]
'Cood'

>>> # Positive Slicing
>>> s = "Simple is better than Complex"
>>> s[9:16]
' better'
>>> s[21:29]
' Complex'
>>> s[0:6]
'Simple'

>>> s2 = "Beautiful is better than Ugly"
>>> s2[0:9]
'Beautiful'
>>> s2[12:19]
' better'
>>> s2[24:29]
' Ugly'

>>> # Negative Slicing
>>> a = "Work Hard Until you succeed"
>>> b = "Vijayawada is a Royal City"

>>> a[-1]
'd'
>>> a[-27:-23]
'Work'
>>> a[-22:-18]
'Hard'
>>> a[-17:-12]
'Until'
>>> a[-11:-8]
'you'
>>> a[-7:]
'succeed'

>>> b[-26:-16]
'Vijayawada'
>>> b[-10:-5]
'Royal'
>>> b[-4:]
'City'

>>> # Positive Striding
>>> a = "Cloud Computing"
>>> a[::]
'Cloud Computing'
>>> a[::3]
'CuCpi'

>>> a = "Data Science"
>>> a[::2]
'Dt cec'
>>> a[::5]
'DSc'

>>> a = "Python Course"
>>> a[0:5]
'Pytho'
>>> a[1:8:3]
'yoC'
>>> a[2:12:3]
'tnos'

>>> # Negative Striding
>>> a = "Machine Learning"
>>> a[::-1]
'gninraeL enihcaM'      # complete reverse
>>> a[::-2]
'gieLenhM'              # every 2nd char from end
>>> a[-1:-8:-2]
'gire'
>>> a[-4:-15:-2]
'naLeic'
>>> a[-2:-16:-5]
'nei'
