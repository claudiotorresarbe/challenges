n = int(input())
 
for x in range(n):
    w = input()
 
    palavra = [x for x in w]
 
    if len(palavra) > 10:
        print(palavra[0]+str(len(palavra)-2)+palavra[-1])
    else:
        print(w)
