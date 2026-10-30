n = int(input())
 
for x in range(n):
    l = list(map(int,input().split(' ')))
 
    print(sorted(l)[1])