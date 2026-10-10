lista = []
qtd = 100
for x in range(0,qtd):
    valor = int(input())
    lista.append(valor)

calc = 0
maior = 0
for y in range(0,qtd):
    maior = (maior+lista[y]+abs(maior-lista[y]))/2

print( int(maior) )
print(lista.index(maior)+1)