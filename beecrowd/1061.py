descricaoinico,diainicio = list(map(str,input().split(' ')))
hor1,min1,seg1 = list(map(int,input().split(' : ')))
descricaofim,diafim = list(map(str,input().split(' ')))
hor2,min2,seg2 = list(map(int,input().split(' : ')))
diainicio = int(diainicio)
diafim = int(diafim)
segundosinicio = (diainicio*24*60*60)+(hor1*60*60)+(min1*60)+seg1
segundosfim =    (diafim*24*60*60)+(hor2*60*60)+(min2*60)+seg2

segundos = 0
minutos = 0
horas = 0
dias = 0

if (segundosfim-segundosinicio) >= 60:
    for x in range(segundosinicio,segundosfim):
        segundos += 1
        if segundos == 60:
            minutos += 1
            segundos = 0
        if minutos == 60:
            horas += 1
            minutos = 0
        if horas == 24:
            dias += 1
            horas = 0

    print(dias,'dia(s)')
    print(horas,'hora(s)')
    print(minutos,'minuto(s)')
    print(segundos,'segundo(s)') 