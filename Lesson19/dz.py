# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#       	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	# 'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	# 'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	# 'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	# 'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

loves = {'я люблю':['шоколад','торт'],
		 'я не люблю':['рыбу','мясо']}

for k,v in loves.items():
	for product in v:
		print(k+' '+product)

a = [5,2,3]
b = [i for i in a]
print(sorted(b))
print(*sorted(b))
print(*sorted(b),sep ='\n' )