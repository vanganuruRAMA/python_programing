
#How to check the mobile nummber
#the mobile number must be 10 digit long
#the mobile number can have 11 digit if including '0' at the starting
#the mobile number can have 12 digit if including '91' at the starting
#first digit should contain nummber between 6-9
#the rest 9 digit can contain any number between 0-9


import re
number=input(" enter mobile number")
result= re.compile("(0|91)?[-\s]")

if result.match(number):
    print(r"is valid mobile number.")
else:
    print(r" is not valid mobile number.")


'''
	
import re	
def isvalid(mob_num):
    pattern = re.compile("(0|91)?[-|s]?[6-9]{0-9}{9}")
    return pattern.match(mob_num)

    mob_num=("enter my  mobile number")
if isvalid(mob_num):
    print(r"{mob_num}is valid mobile number.")
else:
    print(r"{mob_num} is not valid mobile number.")

 '''