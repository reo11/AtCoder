from collections import Counter
s = list(input())
c = dict(Counter(s))
c = sorted(c.items(), key=lambda c: c[1], reverse=True)
print(c[0][0])
