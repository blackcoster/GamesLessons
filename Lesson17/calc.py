def add(num1: float, num2: float) -> float:
    return num1 + num2

def sub(num1: float, num2: float) -> float:
    return num1 - num2

def mul(num1: float, num2: float) -> float:
    return num1 * num2

def div(num1: float, num2: float) -> float:
    return num1 / num2



if __name__=='__main__':
    print('Я запущен как самостоятельная программа')
    num1 = int(input())
    num2 = int(input())
    choice = int(input('Выберите необходимое действие 1: +, 2: -, 3: *, 4: /'))
    match choice:
        case 1:
            print(add(num1,num2))
        case 2:
            print(sub(num1, num2))
        case 3:
            print(mul(num1, num2))
        case 4:
            print(div(num1, num2))


