a = []
while True:
    try:
        n = input()
        a.append(n)
    except:
        break
print(len(set(a)))