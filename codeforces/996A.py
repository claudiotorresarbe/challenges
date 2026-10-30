n = int(input())
 
valor = n
qtd = 0
 
if valor // 100 > 0:
    qtd += valor // 100
    valor = valor - ((valor // 100) * 100)
 
if valor // 20 > 0:
    qtd += (valor // 20)
    valor = valor - ((valor // 20) * 20)
 
if valor // 10 > 0:
    qtd += valor // 10
    valor = valor - ((valor // 10) * 10)
 
if valor // 5 > 0:
    qtd += valor // 5
    valor = valor - ((valor // 5) * 5)
 
if valor // 1 > 0:
    qtd += valor // 1
    valor = valor - ((valor // 1) * 1)
 
print(qtd)