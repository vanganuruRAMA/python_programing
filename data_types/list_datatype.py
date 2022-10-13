data=[14,2,3,4,5,6,7,8,9,1]
fruites=['banana','apple','cherry']
print(type(data))
print(type(fruites))
print(dir(data))

#append
"""
data.append(10)
print(data)
data.append([11,12,13,14])
print(data)
"""

#extend
"""
data.extend([11,12,13,14])
print(data)
"""
#insert
"""
fruites.insert(1,"orange")
print(fruites)             #['apple', 'orange', 'banana', 'cherry']
"""

#pop
"""
fruites.pop(0)
print(fruites)   #['apple', 'banana']
"""

#remove

"""
fruites.remove("apple")
print(fruites)
"""

#clear
"""
fruites.clear()
print(fruites)       #[]
"""

#reverse
"""
fruites.reverse()
print(fruites)
"""

#sort      #order wise
"""
fruites.sort()
print(fruites)
data.sort()
print(data)
"""

#count
"""
count=data.count(14)
print(count)
"""

#index

'''
index=data.index(14)       #position
print(index)
'''

#copy
data2=data.copy()
print(data)
data2.append(50)
print(data2)







