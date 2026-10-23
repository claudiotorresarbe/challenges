a = int(input())
b = int(input())

calc = ( b - (a * 2) ) / 2

if int(calc) == 0 or a > b or int(calc) < 0:
    print('Amelia tem todas bolinhas!')
else:
    print(f'Faltam {int(calc)} bolinha(s)')