# -*- coding: utf-8 -*-
import math

while True:
  try:
    m,n = map(int,input().split(' '))
    print(math.factorial(m)+math.factorial(n))
  except EOFError:
    break