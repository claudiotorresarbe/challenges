n = int(input())

for x in range(0,n):
    a,b,c = input().split(' ')
    print(round(((float(a)*2)+(float(b)*3)+(float(c)*5))/10,1))