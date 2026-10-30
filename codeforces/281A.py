a = input()
 
texto = [x for x in a]
 
texto.insert(0,texto[0].capitalize())
texto.pop(1)
 
print(''.join([x for x in texto]))