#x:x^2
dict1 = {x:x**2 for x in range(5)}
print(dict1)

# AX AY AZ BX BY BZ CX CY CZ
dict2 = {x:y for x in  'ABC' for y in 'XYZ'}
print(dict2)
dict2 ={x:'Z' for x in 'ABC'}
print(dict2)
dict2 = {}.fromkeys('ABC','Z')
print(dict2)
#A0 B1 C2
dict3 = {x:y for x,y in [('a',1),('b',2),('c',3)]}
print(dict3)
#значение = список

dict4 = {x: [y for y in range(x,x+3)] for x in range(4)}
print(dict4)
#проход по строке

dict5 = {x: [y % 2 for y in range(10)] for x in 'ABC'}
print(dict5)

dict6 = {'ABCDE'[i]: [i % 2]*5 for i in [0,1,2,3,4]}
print(dict6)

#словарь в словаре


dict7 = {x: {y: 0 for y in 'XYZ'} for x in 'ABC'}
print(dict7)


dict1 = {x: {y: x for y in 'XYZ'} for x in 'ABC'}


#set в словаре
dict8 = {i:{j for j in [1,2,3,4,4,4,4]}for i in [1,2,3]}
print(dict8)
#условие
dict9 = {x:1 for x in 'ABCDE' if x in 'BCD'}
print(dict9)
#else
dict10 = {x:1 if x in 'BCD' else 0 for x in 'ABCDE'}
print(dict10)












