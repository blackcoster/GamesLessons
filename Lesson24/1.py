def decorator_args(name):
    print(name)
    def decorator(func):
        def wrapper(a, b):
            print('до')
            func(a, b)
            print('после')
            return (a, b)

        return wrapper
    return decorator

@decorator_args('первый вызов')
def add(a,b):
    print(a,b)

add(3,4)