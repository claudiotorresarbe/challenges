n = int(input())
nro = 0
texto = ''
for x in range(1,n+1):
    for y in range(1,5):
        nro += 1
        if y == 4:
            texto = texto + ' ' + 'PUM'
        else:
            if y == 1:
                texto = str(nro)
            else:
                texto = texto + ' ' + str(nro)
    print(texto)
    texto = ''