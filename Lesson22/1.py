def decorator(func):
    def wrapper():
        print('привет! я функция-оболочка')
        func()
    return wrapper

@decorator
def basic():
    print('я маленькая самостоятельная функция')

basic()
