a = int(input())
 
l = list(map(int,input().split()))
 
l2 = []
for x in range(len(l)):
    l2.append(l.index(x+1)+1)
 
print(' '.join([str(x) for x in l2]))
