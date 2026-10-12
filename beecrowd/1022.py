import math

n = int(input())

for x in range(n):
    N1, x1, D1, op, N2, x2, D2 = input().split(' ')
    N1, N2, D1, D2 = int(N1), int(N2), int(D1), int(D2)
    
    if op == '+':
        num = (N1*D2 + N2*D1)
        div = (D1*D2)
    elif op == '-':
        num = (N1*D2 - N2*D1)
        div = (D1*D2)
    elif op == '*':
        num = (N1*N2)
        div = (D1*D2)
    elif op == '/':
        num = (N1*D2)
        div = (N2*D1)

    mdc = math.gcd(num, div)
    num2 = num
    div2 = div
    num2 //= mdc
    div2 //= mdc
    
    print(f'{num}/{div} = {num2}/{div2}')

