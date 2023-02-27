class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass = MyClass()
iterator = iter(myclass)
for i in myclass:
    print(i)
