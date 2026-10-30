a = input()
b = input()
 
lista = [a.lower(),b.lower()]
 
lista2 = sorted(lista)
 
if a.lower() == b.lower():
    print(0)
elif a.lower() != b.lower() and lista2.index(a.lower()) == 0:
    print(-1)
elif a.lower() != b.lower() and lista2.index(a.lower()) == 1:
    print(1)