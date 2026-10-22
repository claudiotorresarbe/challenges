# -*- coding: utf-8 -*-
n = int(input())

for x in range(n):
  o = float(input())
  qtd = 0
  while True:
    if o <= 1:
      print(qtd,'dias')
      break
    qtd += 1
    o -= o/2
