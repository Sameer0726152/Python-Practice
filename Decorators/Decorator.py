from functools import wraps
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def greet():
    print("Hello")
greet()
print(greet.__name__)

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Prefix")
        func()
        print("Suffix")
    return wrapper

@my_decorator
def call():
    print("Come here")

call()
print(call.__name__)