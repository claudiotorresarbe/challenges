a,b = list(map(int,input().split()))
c = input()
 
texto = c
for x in range(b):
    texto = texto.replace('BG','GB')
 
print(texto)