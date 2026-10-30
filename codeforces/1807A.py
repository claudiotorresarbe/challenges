n = int(input())
 
for x in range(n):
    a,b,c = list(map(int,input().split()))
 
    if a + b == c:
        print('+')
    else:
        print('-')