preco_banana,valor_disponivel,quantidade_comprada = list(map(int,input().split(' ')))
 
valor = 0
for x in range(quantidade_comprada+1):
    valor += preco_banana * x
 
total = valor-valor_disponivel
if total < 0:
    print(0)
else:
    print(total)