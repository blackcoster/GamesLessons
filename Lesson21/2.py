class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a +=1
        return x

myclass = MyClass()
iterator = iter(myclass)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
