a,b,c,d = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
d = float(d)

med = ((a*2)+(b*3)+(c*4)+(d*1))/10
print('Media:',round(med,1))
if med >= 7.0:
    print('Aluno aprovado.')
elif med < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= med <= 6.9:
    print('Aluno em exame.')
    e = input()
    e = float(e)
    print('Nota do exame:',e)
    if (e+med)/2 > 5.0:
        print('Aluno aprovado.')
    elif (e+med)/2 <= 4.9:
        print('Aluno reprovado.')
    print('Media final:',(e+med)/2)