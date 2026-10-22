n = int(input())

for n2 in range(0,n):
    x,y = input().split(' ')
    x = int(x)
    y = int(y)
    numero = x
    soma = 0
    qtd = 0
    while True:
        if numero % 2 == 1:
            soma = soma + numero
            qtd += 1
        if qtd == y:
            break
        numero += 1
    print(soma)