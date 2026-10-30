a = int(input())
 
txt = [x for x in str(a)]
 
tam_t = len(txt)
tam_4 = txt.count('4')
tam_7 = txt.count('7')
 
if (tam_4 + tam_7) in{4,7}:
    print('YES')
else:
    print('NO')