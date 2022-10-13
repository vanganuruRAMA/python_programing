data={1,2,3,4,6,5,6,"book","program",9,}
print(type(data))
print(data)
print(dir(data))

data.add("python")
print(data)

a={'apple',"banana",'cherry',"grapes"} 
b={'google','microsoft','apple','grapes'}
#z=a.difference(b)      #only diffence in a  {'banana', 'cherry'}
#z=b.difference(a)       #only diffence in banana  {'microsoft', 'google'}
#print(z)
"""
a.difference_update(b)      #{"banana",'cherry'}
print(a)
b.difference_update(a)   #{'google','microsoft','apple'}
print(b)
"""

#a.discard("banana")    #{'apple', 'cherry'}
#print(a)

#x=a.intersection(b)    #common elements
#print(x)

#x=a.union(b)   
#print(x)

#a.symmetric_difference(b)
#b.symmetric_difference(a)
#print(a)

#a.update(b)
#print(a)

#x=a.issuperset(b)
#x=a.issubset(b)
#print(x)

#print(a&b)
print(a|b)
print(a^b)

#pratice
"""
intersection_update
symmetric_difference_update
pop
copy
"""







