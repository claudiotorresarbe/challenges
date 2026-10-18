x,y = input().split(' ')
x = int(x)
y = int(y)
qtd = 0
texto = ''
if 1 < x < 20 and x < y < 100000:
    for linha in range(1,round((y/x)+0.5)+1):
        for nro in range(1,x+1):
            qtd += 1
            if nro == 1:
                texto = str(qtd)
            else:
                texto = texto + ' ' +str(qtd)
        print(texto)
        if qtd == 99:
            break