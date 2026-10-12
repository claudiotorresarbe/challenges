while True:
  lista = ''
  total = 0
  m,n = input().split(' ')
  m = int(m)
  n = int(n)
  if m <= 0 or n <= 0:
    break;
  else:
    if m > n:
      for x in range(n,m+1):
        if x == n:
          lista = lista + str(x)
          total = total + x
        else:
          lista = lista + ' ' + str(x)
          total = total + x
      print(lista,'Sum='+str(total))
    else:
      for x in range(m,n+1):
        if x == m:
          lista = lista + str(x)
          total = total + x
        else:
          lista = lista + ' ' + str(x)
          total = total + x
      print(lista,'Sum='+str(total))