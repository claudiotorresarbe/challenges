# -*- coding: utf-8 -*-
n = int(input())
lista_a = []
for x in range(n):
  m = int(input())
  lista_a.append(m)

lista_b = lista_a
for x in sorted(set(lista_b)):
  print(x,'aparece',lista_b.count(x),'vez(es)')

