n = int(input())
txt = input()
 
l = [x.lower() for x in txt]
 
print('YES' if len(set(l)) == 26 else 'NO')