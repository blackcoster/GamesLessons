import sys
import time

def get_size(func):
    def wrapper(a,b,delay=0):
        result = sys.getsizeof(func(a,b,delay))
        print(f'{result} байт')
    return wrapper

@get_size
def func(a,b,delay = 0):
    print('начало')
    time.sleep(delay)
    print('посчитал')
    return a*b

a = func(3,4)