# 2003,5,45
from datetime import date

def check(y,m,d):
    try:
        date(y,m,d)
        print('yes')
    except:
        print('no')

check(578970 ,2,29)