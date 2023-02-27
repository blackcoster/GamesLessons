def func(num):
    while num>0:
        yield num
        num-=1

result = func(5)

for num in result:
    if num==2:
        break
    print(num)