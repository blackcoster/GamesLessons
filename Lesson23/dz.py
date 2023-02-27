import datetime
import time

def z():
    time.sleep(5)

a = datetime.datetime.now()
z()
b = datetime.datetime.now()

print(b-a)

