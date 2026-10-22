n = int(input())
total = 0
if 0 < n < 13:
  for x in reversed(range(1,n+1)):
    if x == n:
      total = x
    else:
      total = total * x
print(total)