n = int(input())
 
result = []
for x in range(n):
    p = input()
    
    texto = p.replace('X','')
    texto = texto.replace('++','1')
    texto = texto.replace('--','2')
 
    result.append(texto)
 
print(sum([-1 if int(z) == 2 else int(z) for z in result]))