l1 = input()
l2 = input()
 
texto = ''
for x in range(len(l1)):
 
    if l1[x] == l2[x]:
        texto += '0'
    else:
        texto += '1'
 
print(texto)