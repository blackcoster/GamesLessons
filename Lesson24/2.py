i = int(input())
def decorator_args(n):
    print(n)
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@decorator_args(i)
def hello():
    print('hello')

hello()