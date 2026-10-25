import math

def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    s = [math.exp(x - m) for x in scores]
    t = sum(s)
    r = [ round(x / t,4) for x in s]
    return r

#print([round(x, 4) for x in softmax([1000, 2000, 3000])])
print(softmax([1000, 2000, 3000]))
