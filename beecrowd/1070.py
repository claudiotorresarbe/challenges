a = int(input())
rodada = 0
while True:
    if a % 2 == 1:
        print(a)
        rodada += 1
    if rodada == 6:
        break
    a += 1