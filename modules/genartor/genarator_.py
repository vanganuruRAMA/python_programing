'''
def get_next_num ():
    n=1
    print("this is first print")
    yield n
    n+=1
    print("this is second print")
    yield n
    n+=2
    print("this is third print")
    yield n
data=get_next_num()
print(next(data))
print(next(data))
print(next(data))
'''
#gen
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i
a = sq_numbers(5)
  
print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
