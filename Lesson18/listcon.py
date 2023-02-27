# # список вручную
# list1 = []
# for i in range(1,11):
#     list1.append(i)
#
# print(list1)
# #список включением
# list1 = [i for i in range(1,11)]
# print(list1)
# #список квадратов
# list2 = [i**2 for i in range(1,11)]
# print(list2)
# #строчные значения
# list3 = [str(i) for i in [1,2,3]]
# print(list3)
#из консоли
# list4 = [int(i) for i in input().split()]
# print(list4)
#с условием
list5 = [i for i in range (1,101) if i%2==0]
print(list5)
#два цикла
list6 = [i*j for i in range(1,10) for j in [1,2,3]]
print(list6)
#два цикла два условия
list7 = [i*j for i in range(1,10) for j in [1,2,3] if i%2==0 if j!=2]
print(list7)
#кортеж
tuple1 = tuple([i for i in range (1,10)])
print(type(tuple1))