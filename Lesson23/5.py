class Polina:
    def __init__(self,func):
        self.func = func


    def __call__(self,name):
        print('начало')
        self.func(name)
        print('конец')

@Polina
def say(name):
    print('hello',name)

# obj = Polina(say)
# obj()

say('polina')