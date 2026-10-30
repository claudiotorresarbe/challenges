n = int(input())
 
for x in range(n):
    p = int(input())
    l = list(map(int,input().split()))
 
    a,b = set(l)
    
    if l.count(a) > l.count(b):
        print(l.index(b)+1)
    else:
        print(l.index(a)+1)