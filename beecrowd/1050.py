n = int(input())

ddd = [61,71,11,21,32,19,27,31]
des = ['Brasilia','Salvador','Sao Paulo','Rio de Janeiro','Juiz de Fora','Campinas','Vitoria','Belo Horizonte']

try:

    print(des[ddd.index(n)])

except:
    print('DDD nao cadastrado')
