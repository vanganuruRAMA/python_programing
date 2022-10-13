#    Regular expression

'''
search
match
findall
sub
'''

# modifiers
'''
\d # any digit match
\w # any charectors
\W # any string does match
\s # space 
\t # tab
\D # matches non digits
'''

#Character	Description	
'''
[]	A set of characters	
\	Signals a special sequence (can also be used to escape special characters)	
.	Any character       #(except newline character)	
^	Starts with	       #(matches beginning of line)	
$	Ends with          #(matches end of line)		
*	Zero or more occurrences	
+	One or more occurrences	
?	Zero or one occurrences	
{}	Exactly the specified number of occurrences	
|	Either or		
()	Capture and group	 
'''
# flags
'''
re.M | re.I
'''
import re

data='this is module 567,2,8 method'
#res=re.search(r'\d',data)
#res=re.search(r'\d+,\d+',data)
res=re.search(r'.+',data)
print(res.group())

string = '39801 356, 2102 1111'   #out 80135

result=re.search(r'(\d{3}) (\d{2})',string)
print(result.group(1))
print(result.group(2))

line = "cats77 are Smarter then dogs"

#result=re.match(r'(.*) are (.*?) .* (\w+$)',line)
result=re.match(r'(.*) are (.*?) (.*) (\w+$)',line)
print(result.group(2),result.group(3))

#mobile_Nos= 'You can reach me out at +12223334444 and +919985797628 this is 9985792'
number= '9985797628'
result=re.search(r'\d[1:9]',number)
print(result.group())

# Findall  (writen in list)

data="""Siva  is 23 years old, Jagan  is 40 years old 
and Venky  is 25  years and Bharath  is 25  
years old his firnds  of sure"""
age=re.findall(r'\d{1,2}',data)
names=re.findall(r'[A-Z][a-z]+',data)
print(age)
print(names)
'''
data='yasodha234@gmail.com'
result=re.match(r'\w+@\w+.\w*',data)
print(result.group())
'''
email = "abceautomation.12345@gmail.com"
#result=re.match(r'\w+.\w+@',email)
result=re.match(r"\w+[/.|\w]+@(\w+[.])*(com|in|govt)", email)
print(result.group())

# sub

data='iam software engineer'
result=re.sub(r'engineer','testing automation',data)
print(result)