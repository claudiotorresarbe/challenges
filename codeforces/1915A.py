n = int(input())
 
for x in range(n):
    l = list(map(int,input().split(' ')))
 
    for x in set(l):
        if l.count(x) == 1:
            print(x)
            break