#Regular expenssion
'''
suts
match
find 
all


# modifiers

.  # any charector match
\d # any digit match
\w # any charectors
\W # any strimg does match
\s # space 
\t # tab
$  # ending mach
^  #stars with mach
*  #0 or o
\D #


#Character	Description	

[]	A set of characters	
\	Signals a special sequence (can also be used to escape special characters)	
.	Any character (except newline character)	
^	Starts with		
$	Ends with		
*	Zero or more occurrences	
+	One or more occurrences	
?	Zero or one occurrences	
{}	Exactly the specified number of occurrences	
|	Either or		
()	Capture and group	 
'''


import re
data="this is module 8954,56,2,8 methods"
#res=re.search(r"\d+",data)   #ouput  8954
#res=re.search(r"\d.",data)    #out  89
#res=re.search(r"\w.",data)     #th
#res=re.search(r"\w",data)     #t
#res=re.search(r"\s+",data)      # empt
#res=re.search(r"\t",data)
#res=re.search(r"\w+",data)       #this
#res=re.search(r".+",data)      
res=re.search(r".+,+.",data)      

#res=re.search(r"\w+,",data)       #this
#res=re.search(r"\w+,\d+,\d+",data)   #8954,56,2    
#res=re.search(r"\w+,\d+,\d*",data)   
#res=re.search(r"\w+,\d+,\d*",data) 

  
#print(res.group())
#print(res.group())
#print(res.group())
#print(res.group())

'''
import re

data='this is module 567,2,8 method'
#res=re.search(r'\d',data)
#res=re.search(r'\d+,\d+',data)
res=re.search(r'.+',data)
print(res.group())
'''




line = "cats77 are Smarter then dogs"

#result=re.match(r'(.*) are (.*?) .* (\w+$)',line)
#result=re.match(r'(.*) are (.*?) (.*) (\w+$)',line)
#result=re.match(r'(.*) are (.+),line)
#print(result.group(1),result.group(2))


email = "abceautomation.12345@gmail.com"
#result=re.match(r'\w+.\w+@',email)
#result=re.match(r"\w+[/.|\w]+@(\w+[.])*(com|in|govt)", email)
#print(result.group())

data='1234567890'
result=re.match(r'(0:9)+',data)
#print(result.group())


number= '9985797628'
result=re.search(r'\d[1:9]+',number)
print(result.group())


'''
import re
number=input(" enter mobile number")
pattern=re.compile("(0|91)?[-\s]?[6-9]{0-9}{9}")

if pattern.match(number):
    #print(r"{number}is valid mobile number.")
else:
    #print(r"{number} is not valid mobile number.")

'''

import re
data= " " " Siva  is 23 years old, Jagan  is 40 years old 
and Venky  is 25  years and Bharath  is 25  
years old his firnds  of sure" " "
age=re.findall(r'\d{1,2}',data)
names=re.findall(r'[A-Z][a-z]+',data)
print(age)
print(names)

