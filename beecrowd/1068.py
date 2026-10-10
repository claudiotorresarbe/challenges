while True:
  try:
    n = input()
    qtd = 0
    for x in n:
      if x == '(':
        qtd += 1
      elif x == ')':
        qtd -= 1
      if qtd == -1:
        break
    if qtd == 0:
      print('correct')
    else:
      print('incorrect')
  except EOFError:
    break