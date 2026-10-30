a = input()
b = input()
 
txt = ''.join([x for x in a][::-1])
 
if txt == b:
    print('YES')
else:
    print('NO')
