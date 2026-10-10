n = float(input())

nivel = 0

if 0 < n <= 2000.00:
    nivel = 0
elif 2000.01 <= n <= 3000.00:
    nivel = 1
elif 3000.01 <= n <= 4500.00:
    nivel = 2
elif n > 4500.00:
    nivel = 3

if nivel == 0:
    print('Isento')
if nivel == 1:
    print('R$','%.2f'%((n-2000)*0.08))
if nivel == 2:
    print('R$','%.2f'%((1000)*0.08+(n-3000)*0.18))
if nivel == 3:
    print('R$','%.2f'%((1000)*0.08+(1500)*0.18+(n-4500)*0.28))