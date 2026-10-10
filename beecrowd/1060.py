total = 0
rodada = 0
while rodada < 6:
    a = input()
    if len(a) > 0:
        if float(a) > 0:
            total += 1
        rodada += 1

print(total,'valores positivos')