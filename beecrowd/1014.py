var_a = var_b = 0
for x in range(1,3):
    a = float(input())
    if x == 1:
        var_a = a
    else:
        var_b = a

print(str(round(var_a/var_b,3)),'km/l')
