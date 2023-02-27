import time
from functools import cache

@cache
def func(n):
    result=0
    for i in range(n):
        result+=i
    return result

start = time.time()
print(func(30_000_000))
end = time.time()
print(end-start)

start2 = time.time()
print(func(30_000_000))
end2 = time.time()
print(end2-start2)
