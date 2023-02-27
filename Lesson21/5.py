class MyClass:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        x = self.start
        while x < self.stop:
            yield x
            x+=self.step

nums = MyClass(0.0,1.0,0.1)
# for x in nums:
#     print(x)

print(0.1+0.2)