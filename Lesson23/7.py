
import time

def get_size(func):
    def wrapper(a,b,delay=0):
        print(type(func(a,b,delay)))
    return wrapper

@get_size
def func(a,b,delay = 0):
    print('начало')
    time.sleep(delay)
    print('посчитал')
    return a*b


a = func(3,4)
