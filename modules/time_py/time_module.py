import time
'''
print(time.time()) #epoch time
current_human=time.ctime(1663640146.7837322)
print(current_human)
current_local=time.localtime(1663640146.7837322)
print(current_local)
current_gmtime=time.gmtime(1663640146.7837322)
print(current_gmtime)
'''
from time import gmtime, strftime
 
# using simple format of showing time
s = strftime("%a-%d-%b-%Y %H:%M:%S",
             gmtime(1663640146.7837322))
print(s)
