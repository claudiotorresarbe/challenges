a = int(input())
ano = a + 1
while True:
    
    txt = [x for x in str(ano)]
    
    a1 = txt.count(txt[0])
    a2 = txt.count(txt[1])
    a3 = txt.count(txt[2])
    a4 = txt.count(txt[3])
 
    if 1 == a1 == a2 == a3 == a4:
        print(ano)
        break
    ano += 1