a,b,c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

if a+b <= c or a+c <= b or c+b <= a:
    print('Area =',((a+b)*c)/2)
else:
    print('Perimetro =',(a+b+c))