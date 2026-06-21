from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Brewing : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished : {func.__name__}")
        return result
    return wrapper

def brew(type, milk, sugar):
    print(f"I want {type} chai, {milk} milk, {sugar} gm sugar")
brew("Masala", "No", 50)