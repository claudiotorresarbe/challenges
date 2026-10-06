m,n = input().split(' ')

if int(m) < int(n):
    print('O JOGO DUROU',int(n) - int(m),'HORA(S)')
else:
    print('O JOGO DUROU',int(n)+24 - int(m),'HORA(S)')