t = input()
 
texto = [x.isupper() for x in t]
 
if texto.count(True) > texto.count(False):
    print(t.upper())
else:
    print(t.lower())