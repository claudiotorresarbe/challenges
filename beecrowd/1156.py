c = 0
s = 0
b = 1
for a in range(1,40,2):
    c = a/b
    s += c
    b *= 2

s = (round(s,2))
print(format(s,'.2f'))