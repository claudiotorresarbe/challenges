import math
a,b,c = list(map(float,input().split(' ')))
if a != 0 and b != 0 and c != 0:
    try:
        delta = b**2-4*a*c
        x = ((b*-1)+math.sqrt(delta))/(2*a)
        y = ((b*-1)-math.sqrt(delta))/(2*a)
        print('R1 =','%.5f'%x)
        print('R2 =','%.5f'%y)
    except:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')