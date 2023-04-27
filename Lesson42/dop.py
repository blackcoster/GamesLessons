x = 'polina'

def func():
    global x
    x = 'lena'
    print(f'hello {x}')

func()
print(x)