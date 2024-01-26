import itertools
from math import ceil

t = []
for i in range(5):
    t.append(int(input()))
ans = 10**9

for values in list(itertools.permutations(t)):
    tmp = 0
    for i, v in enumerate(values):
        if i == 4:
            tmp += v
        else:
            tmp += ceil(v / 10) * 10
    ans = min(ans, tmp)
print(ans)
