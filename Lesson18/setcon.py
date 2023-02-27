
#Условие if указывается после объявления цикла и итерируемого объекта:

set1 = {i for i in  ['ab_1', 'ac_2', 'bc_1', 'bc_2']if 'a' not in i}
print(set1)

#
#Условное выражение if... else... указывается до объявления цикла:

set2 ={'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2']}
print(set2)
ans = 'polina'
bans = ans[2:4]
print(bans)

