f = open('1.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))

except ValueError:
    print('Это не число')
except Exception:
    print('это что вообще такое?')

finally:
    f.close()
    print('закрыт')
