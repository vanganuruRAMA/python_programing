import time

print(time.time())
current_human=time.ctime(1663647821.9766355)
print(current_human)
current_local=time.localtime(1663647821.9766355)
print(current_local)
current_gmtime=time.gmtime(1663647821.9766355)
print(current_gmtime)

print(time.time())
print(time.asctime())

start=time.time()
now=time.gmtime()
now=time.asctime(now)
print(now)
stop=time.time()
print(start-stop)
time.sleep(3)

now=time.gmtime()
print(now[1])

from time import gmtime,strftime


s = strftime("%a,%d-%b-%Y %H:%M:%S",
             gmtime(1663640146.7837322))
print(s)



string = "Tue, 03 Aug 2021 10:45:08"
obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")

print(obj)


data="2018-02-01 11:33:33.999"
res=time.strftime(data,"%A")
print(res)




