a = input('Введите время ')
hour,min =a.split(':')
hour = int(hour)
min = int(min)
if hour>12:
    hour = hour-12
if hour==0:
    hour =12
print('короткая стрелка ', hour)

if min%5!=0:

    min1=min//5
    min2 =min//5+1
    if min1==0:
        min1=12
    print('длинная стрелка между ',min1,' и ',min2)

else:
    min=min//5
    if min==0:
        min=12
    print('длинная стрелка на', min)




