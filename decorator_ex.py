def log(func):
    def wrapper(*args, **kwargs):
        print(f"Doing '{func.__name__}' function")
        result = func(*args, **kwargs)
        print(f"Result : {result}")
        return result

    return wrapper


@log
def add(a, b):
    return a + b


@log
def multiply(a, b):
    return a * b


add(2, 3)
multiply(4, 5)

print("\n            *********     End First project     *********\n")

from functools import wraps


user = {"username": "ali", "is_admin": False}


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user["is_admin"]:
            print(f"Access denied for {user['username']}")
        else:
            func(*args, **kwargs)
    return wrapper

@require_admin
def delete_all_users():
    print("All users deleted.")


delete_all_users()
