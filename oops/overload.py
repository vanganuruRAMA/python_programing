#overload
'''
python does not support method overloading by default.
 But there are different ways to achieve method overloading in Python. 
The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 
'''
def sum(a,b):
    data=a+b
    print(data)
def sum(a,b):
    data=a+b
    print("hi",data)
sum(10,20)