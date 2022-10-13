#Decorators
'''
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
without permanently modifying it
'''



def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print(args, kwargs)
    return inner_decorator

@decorator
def decorated(string_args):
    print("This happened : " + string_args)

#if _name_ == "__main__":
decorated("Hello, how are you?")




'''
def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print("This function takes " + str(len(args)) + " arguments")
        inner(*args)

    return inner_decorator


@decorator
def decorated(string_args):
    print("This happened: " + str(string_args))


@decorator
def alsoDecorated(num1, num2):
    print("Sum of " + str(num1) + "and" + str(num2) + ": " + str(num1 + num2))


#if _name_ == "__main__":
decorated("Hello yes fine")
alsoDecorated(1,10)
'''