f = open('test.txt')
lines = (t.strip() for t in f)
comments = (t for t in lines if t[0] =='#')
for num in comments:
    print(num)

comments_list = list(comments)
print(comments_list)
