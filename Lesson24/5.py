from functools import wraps

def decorator(func):
    """Функция-декоратор"""
    @wraps(func)
    def wrapper():
        """функция-обертка"""
        func()
    return wrapper


@decorator
def hello():
    """здороваемся"""
    print('hello')

print(hello.__name__)
help(hello)