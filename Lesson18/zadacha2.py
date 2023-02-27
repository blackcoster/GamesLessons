dict1 = {'b':2,
 'd':4,
 'a':1}

# a=1 b=2 d=4

def query(a):
    b=  sorted([f'{k}={v}' for k,v in dict1.items()])
    c= ' поля '.join(b)
    return c

print(query(dict1))

# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)
