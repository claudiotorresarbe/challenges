a = input()
 
texto = set([x for x in a])
 
if len(texto) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')