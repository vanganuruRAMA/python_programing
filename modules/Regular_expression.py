#    Regular expression

'''
suts
match
find 
all
'''

# modifiers
'''
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
'''

#Character	Description	
'''
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
result=re.search(r'\d[0-9]',number)
print(result.group())
