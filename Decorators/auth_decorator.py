from functools import wraps
def auth_deco(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied, Admins only")
            return None
        else :
            return func(user_role)
    return wrapper
@auth_deco
def access_tea(role):
    print("Access tea inventory")
    
access_tea("admin")
access_tea("employee")
            