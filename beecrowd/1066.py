lista = []
for x in range(0,5):
    a = int(input())
    lista.append(a)

pares = [x+1 for x in lista if x % 2 == 0]
impares = [x+1 for x in lista if x % 2 == 1]
posit = [x+1 for x in lista if x > 0]
negat = [x+1 for x in lista if x < 0]

print(len(pares),'valor(es) par(es)')
print(len(impares),'valor(es) impar(es)')
print(len(posit),'valor(es) positivo(s)')
print(len(negat),'valor(es) negativo(s)')