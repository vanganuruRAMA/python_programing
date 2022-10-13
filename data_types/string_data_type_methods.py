data=" String datatype is used to hold texts. String values should be placed within "
data2={"name":"python", "type": "interpeter"}
print(data.upper())         	                    #Converts all lowercase characters in a string into uppercase
print(data.capitalize())	                        #Converts the first character of the string to a capital (uppercase) letter
print(data.casefold())	                            #Implements caseless string matching        
print(data.center(20))	                            #Pad the string with the specified character.
print(data.count("d"))	                            #Returns the number of occurrences of a substring in the string.
print(data.encode())	                            #Encodes strings with the specified encoded scheme
print(data.endswith("s"))	                        #Returns “True” if a string ends with the given suffix
print(data.expandtabs())                            #Specifies the amount of space to be substituted with the “\t” symbol in the strin
print(data.find("i"))	                            #Returns the lowest index of the substring if it is found
print("format  {}".format(data))	                #Formats the string for printing it to console
print("{name}  is {type}".format_map(data2))        #Formats specified values in a string using a dictionary
print(data.index("u"))	                            #Returns the position of the first occurrence of a substring in a string
print(data.isalnum())	                            #Checks whether all the characters in a given string is alphanumeric or not
print(data.isalpha())	                            #Returns “True” if all characters in the string are alphabets
print(data.isdecimal())                             #Returns true if all characters in a string are decimal
print(data.isdigit())	                            #Returns “True” if all characters in the string are digits
print(data.isidentifier())	                        #Check whether a string is a valid identifier or not
print(data.islower())	                            #Checks if all characters in the string are lowercase
print(data.isnumeric())	                            #Returns “True” if all characters in the string are numeric characters
print(data.isprintable())	                        #Returns “True” if all characters in the string are printable or the string is emp
print(data.isspace())	                            #Returns “True” if all characters in the string are whitespace characters
print(data.istitle())	                            #Returns “True” if the string is a title cased string
print(data.isupper())	                            #Checks if all characters in the string are uppercase
print(" ".join(data))                               #Returns a concatenated String
print(data.ljust(20))	                            #Left aligns the string according to the width specified
print(data.lower())	                                #Converts all uppercase characters in a string into lowercase
print(data.lstrip())	                            #Returns the string with leading characters removed
print(data.maketrans("S", "P"))	                    #Returns a translation table
print(data.partition("used"))	                    #Splits the string at the first occurrence of the separator 
print(data.replace("hold", "stop"))	                #Replaces all occurrences of a substring with another substring
print(data.rfind("datatype"))	                    #Returns the highest index of the substring
print(data.rindex("datatype"))	                    #Returns the highest index of the substring inside the string
print(data.rjust(20))	                            #Right aligns the string according to the width specified
print(data.rpartition("used"))	                    #Split the given string into three parts
print(data.rsplit())	                            #Split the string from the right by the specified separator
print(data.rstrip())	                            #Removes trailing characters
print(data.splitlines())	                        #Split the lines at line boundaries
print(data.startswith("S"))	                        #Returns “True” if a string starts with the given prefix
print(data.strip())	                                #Returns the string with both leading and trailing characters
print(data.swapcase())	                            #Converts all uppercase characters to lowercase and vice versa
print(data.title())	                                #Convert string to title case
#print(data.translate())	                        #Modify string according to given translation mappings
print(data.zfill(10))	                            #Returns a copy of the string with ‘0’ characters padded to the left side of the string