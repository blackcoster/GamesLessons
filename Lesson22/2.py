# хлеб
# помидор
# котлета
# салат
# хлеб

def bulka(func):
    def wrapper():
        print('bread')
        func()
        print('bread')
    return wrapper

def ingredients(func):
    def wrapper():
        print('tomato')
        func()
        print('salad')
    return wrapper

@ingredients
@bulka
def sandwich():
    print('kotleta')

sandwich()
