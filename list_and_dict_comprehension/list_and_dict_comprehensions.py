#List Comprehensions
#dict  Comprehensions




data=[1,2,3,4,5,6,7,8,9,10]
for i in data:
    if i%2==0:
        print(i)


#List Comprehensions
print([i for i in data if i%2==0])


print([i for i in range(1,50) if i%2==0])    #even number
print([i for i in range(1,50) if i%2==1])    #odd number
print([i for i in range(1,100) if not [j for j in range(2,i)if not i%j]])    #prime number

#dict  Comprehensions
q=["school","college","graduation"]
a=["sarojini","bhavana","vedavyasa"]
print({k:v for (k,v) in zip(q,a)})

data=[1,2,3,4,5]
print({k:k*k for k in data})
print({k:k*k for k in range(1,100)})

