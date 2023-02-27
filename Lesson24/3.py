class Decorator:
    def __init__(self,n):
        print(n)
        self.n = n
    def __call__(self,func):
        def wrapper(a,b):
            print('до')
            for i in range(self.n):
                func(a,b)
            print('после')
        return wrapper

@Decorator(9)
def add(a,b):
    print(a,b)

add(3,4)