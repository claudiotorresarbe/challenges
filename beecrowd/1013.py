a,b,c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

d = (a+b+abs(a-b))/2

valor = (c+d+abs(c-d))/2

print(int(valor),'eh o maior')