a = float(input())
b = float(input())


valor = round(((a*3.5)+(b*7.5))/11,5)

if 0 <= a <= 10 and 0 <= b <= 10:
    print('MEDIA = '+'%.5f'%valor)