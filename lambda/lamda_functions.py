#  lambda functions    (name less,single line operation )

"""
map
filter
reduce
"""
data=lambda a,b : a+b
print(data(10,20))


# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

#    map

numbers=[1,2,3,4,5,6]
print(list(map(lambda n:2*n,numbers)))

print(list(map(lambda n:n*n,[1,2,3,4,5,6])))

names=['yasodha','python','program']
print(list(map(lambda n:n.upper(),names)))

#    filter

numbers=[1,2,3,4,5,6,7,8,9,10]
print(tuple(filter(lambda n:n%2==1,numbers)))   #odd numbers  (1, 3, 5, 7, 9)
print(tuple(filter(lambda n:n%2==0,numbers)))   #even numbers  (2, 4, 6, 8, 10)
#print(list(filter(lambda)))

data=['apple','cherry','grapes','banana','and','sum','names','books']
print(list(filter(lambda s:len(s)>5,data)))
print(list(filter(lambda s:len(s)>2,data)))
print(list(filter(lambda s:len(s)>3,data)))

#   reduce

import functools
numbers=1,2,3,4,5,6,7,8,9,10
print(functools.reduce(lambda a,b:a+b,numbers))