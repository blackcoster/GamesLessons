def decorator(func):
    def wrapper(*args,**kwargs):
        print('начало')
        func(*args,**kwargs)
        print('конец')
    return wrapper

@decorator
def say(*args,**kwargs):
    print('hello',args,kwargs)

say('polina','yana','fedor')