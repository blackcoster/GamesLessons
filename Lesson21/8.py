# s = input()
# ans = ''
# anscnt = 0
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now==s[j]:
#             nowcnt+=1
#     if nowcnt>anscnt:
#         ans = now
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

s = input()
anscnt = 0
symcnt = {}
for now in s:
    if now not in symcnt:
        symcnt[now] =0
    symcnt[now]+=1
    if symcnt[now]>anscnt:
        ans = now
        anscnt = symcnt[now]
print(ans)


