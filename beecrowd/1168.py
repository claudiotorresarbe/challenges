# -*- coding: utf-8 -*-

a = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

n = int(input())

for x in range(n):
    l = input()
    qtd = 0
    for z in l:
        qtd += a.get(z)
    print(str(qtd)+' leds')
