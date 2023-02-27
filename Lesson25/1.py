from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(a,b):
        func(a,b)
    return wrapper


@decorator
def add(a,b):
    """Функция складывает числа"""
    print(a+b)

add(3,4)
print(add.__name__)
print(add.__doc__)

