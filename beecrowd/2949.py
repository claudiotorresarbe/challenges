a = int(input())

l = []
for b in range(a):
    x, y = input().split(' ')
    l.append(y)

r = [
    ['Hobbit(s)','X'],
     ['Humano(s)','H'],
     ['Elfo(s)','E'],
     ['Anao(oes)','A'],
     ['Mago(s)','M']
]
for c,d in r:
    print(l.count(d), c)