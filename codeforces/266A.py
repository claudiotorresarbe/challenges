a = int(input())
l = input()
 
texto = [x for x in l]
 
qtd = 0
 
for x in range(a-1):
    if texto[x] == texto[x+1]:
        qtd += 1
 
print(qtd)