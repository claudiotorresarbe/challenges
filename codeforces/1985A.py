n = int(input())
 
for x in range(n):
 
    a, b = list(map(str,input().split(' ')))
 
    aa = [y for y in a]
    bb = [z for z in b]
    
    aa.insert(0,bb[0])
    bb.insert(0,aa[1])
 
    aa.pop(1)
    bb.pop(1)
 
    af = ''.join([x for x in aa])
    bf = ''.join([x for x in bb])
    print(af,bf)