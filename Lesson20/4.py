def func():
    while True:
        n = yield
        print(n)

r = func()
r.send(None)
r.send(1)
r.send(5)
r.send(6)
r.close()
r.send(1)