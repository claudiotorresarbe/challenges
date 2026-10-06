x = float(input())

if 0 < x <= 400:
  a = 0.15
  print('Novo salario:', '%.2f'%(x+(x*a)))
  print('Reajuste ganho:', '%.2f'%(x*a))
  print('Em percentual:', str(int(a*100))+' %')

if 400 < x <= 800:
  a = 0.12
  print('Novo salario:', '%.2f'%(x+(x*a)))
  print('Reajuste ganho:', '%.2f'%(x*a))
  print('Em percentual:', str(int(a*100))+' %')

if 800 < x <= 1200:
  a = 0.10
  print('Novo salario:', '%.2f'%(x+(x*a)))
  print('Reajuste ganho:', '%.2f'%(x*a))
  print('Em percentual:', str(int(a*100))+' %')

if 1200 < x <= 2000:
  a = 0.07
  print('Novo salario:', '%.2f'%(x+(x*a)))
  print('Reajuste ganho:', '%.2f'%(x*a))
  print('Em percentual:', str(int(a*100))+' %')

if 2000 < x:
  a = 0.04
  print('Novo salario:', '%.2f'%(x+(x*a)))
  print('Reajuste ganho:', '%.2f'%(x*a))
  print('Em percentual:', str(int(a*100))+' %')