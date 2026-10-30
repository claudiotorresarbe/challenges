a,b,c = list(map(int,input().split()))
 
medio = (a+b+c)/3
 
l = []
l.append(abs(a - medio))
l.append(abs(b - medio))
l.append(abs(c - medio))
result = sum(sorted(l,reverse=True)[0:2])
 
print(int(result))