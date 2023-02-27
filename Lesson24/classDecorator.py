import datetime

def timer(cls):
    def wrapper():
        start = datetime.datetime.now()
        cls()
        end = datetime.datetime.now()
        print(end-start)
        # return result
    return wrapper

@timer
class Myclass:
    pass

obj = Myclass()
