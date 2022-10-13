#check for the ip address
#the ip address must be four integer ranging from 0 to 255
#the sperator by three dots
#for exm;0.0.0.0 to 255.255.255.255
#the decimal values of each part of the ip address
#should not exceeds 255 and must not be less than zero

#0-99--->[1-9]?[0-9]
#100-199--->1[0-9][0-9]
#200-249--->2[0-4][0-9]
#250-255--->25[0-5]



import re

IP=input("enter the ip address")
result="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]\.){3} $"
if re.search(IP,result):
    print(r"{IP} is valiad ip address")
else:
    print(r"{IP} is valiad ip address")
	