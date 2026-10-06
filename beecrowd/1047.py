a,b,c,d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

inicio = (a*60+b)
fim = (c*60)+d

if inicio == fim:
    inicio = (0*60+b)
    fim = (24*60)+d
elif inicio > fim:
    inicio = (a*60+b)
    fim = (24*60)+(c*60)+d

if 1 <= fim - inicio <= 24*60:
    contador = 0
    horas = 0
    for x in range(inicio,fim):
        contador += 1
        if contador == 60:
            horas += 1
            contador = 0

    print(f'O JOGO DUROU {horas} HORA(S) E {contador} MINUTO(S)')