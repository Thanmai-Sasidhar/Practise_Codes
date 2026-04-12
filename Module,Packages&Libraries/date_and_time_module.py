
#date and time module
'''
from datetime import date
 
a=date.today()
print(a)

import datetime
b=datetime.datetime.now()
print(b)
'''

import time
'''
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"Today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"Today time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"{b.tm_wday}-{b.tm_mday}-{b.tm_yday}") #Not clear one 
'''
