# One-stroke Path
import itertools

n, m = map(int, input().split())
ab = {}
for i in range(n + 1):
    ab[i] = []
for i in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)

count = 0

for values in list(itertools.permutations(range(2, n + 1))):
    pre = 1
    for i, v in enumerate(values):
        if v not in ab[pre]:
            break
        if i == n - 2:
            count += 1
        pre = v
print(count)
