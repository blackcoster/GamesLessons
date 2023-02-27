from calc import mul,div,sub,add

while True:
    num1 = int(input('число 1 '))
    num2 = int(input('число 2 '))
    choice = int(input(' действия: 1=+, 2=-, 3= *, 4=/,0=вых\n'))
    match choice:
        case 0:
            break
        case 1:
            print(add(num1, num2))
        case 2:
            print(sub(num1, num2))
        case 3:
            print(mul(num1, num2))
        case 4:
            print(div(num1, num2))
        case _:
            print('неверно')
