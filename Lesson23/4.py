class Polina:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print('начало')
        self.func()
        print('конец')

@Polina
def say():
    print('hello')

# obj = Polina(say)
# obj()

say()