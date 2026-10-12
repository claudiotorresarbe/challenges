while True:
  try:
    p,n = map(int,input().split())
    if 0 == p == n:
      break
    val = str(n).replace(str(p),'')
    if len(val) == 0:
      print(0)
    else:
      print(int(val))
  except EOFError:
    break