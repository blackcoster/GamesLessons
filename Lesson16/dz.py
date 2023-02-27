class Test(int):
    def __init__(self, number) :
        super().__init__()
        self.number = number

    def __add__(self, number2):
        self.number2 = number2
        return (f"Произвелось сложение числа {self.number} на {self.number2}")

    def __sub__(self, number2):
        self.number2 = number2
        return (f"Произвелось вычитание из числа {self.number} на {self.number2}")

    def __mul__(self, number2):
        self.number2 = number2
        return (f"Произвелось умножение числа {self.number} на {self.number2}")

    def __truediv__(self, number2):
        self.number2 = number2
        return (f"Произвелось деление числа {self.number} на {self.number2}")

a = Test(10)

print(a + 5)
print(a - 5)
print(a * 5)
print(a / 5)

