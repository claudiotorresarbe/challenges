a = list(map(int,input().split('+')))
 
print('+'.join([str(x) for x in sorted(a)]))