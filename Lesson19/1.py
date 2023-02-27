# mylist = [x*x for x in [1,2,3]]
# for i in mylist:
#     print(i)

numbers =[1,2,3,4,5]
result = (x*x for x in numbers)


# print(result)

for num in result:
    print(num)

print(next(result))



