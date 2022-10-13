#decorators
'''
def login_requred(f1):
    def inner(name,is_login):
        if is_login==False:
            print("kindly login")
            return
        return f1(name,is_login)
    return inner


@login_requred
def home(name,is_login):
    print("welcom to my home page")

@login_requred
def order(name,is_login):
    print("welcom to oder my home page")
def about():
    print("welcom to about my web page")



home(user,False)
order(user,True)
about()

'''
'''

def decorator(inner):
    def inner_decorator(*args,**kwargs):
        print(args,kwargs)
    return inner_decorator

@decorator
def decorator(string_args):
    print("this is :"+ string_args)



#if __name__='main'
decorator("hello")

def decor_result(result_function):
    def distinction(marks):
        for i in marks:
            if i>=75:
                print("distinction")
        result_function(marks)
    return distinction


@decor_result

def result(marks):
    for i in marks:
        if i>=35: 
            pass
        else:
            print("file")
            break
    else:
            print("Pass")

result((35,50,40,75,20))


'''



def f (function):
    def warpper (*args,**kwargs):
        print("start")
        function(*args,**kwargs)
    return("ended")


@f
def f1(a):
    print(a)
f1("hi")

def add (x,y):
    print(x+y)

add(10,20)








