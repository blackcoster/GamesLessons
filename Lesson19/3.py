def func(num):
    while num>0:
        yield num
        num-=1

# for num in func(5):
#     print(num)

a = sum(func(5))
print(a)
# result = func(5)
# # for num in result:
# #     print(num)
#
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))