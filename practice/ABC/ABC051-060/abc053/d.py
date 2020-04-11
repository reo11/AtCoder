from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = len(set(a))
d = defaultdict(int)
for v in a:
    d[v] += 1

cnt = 0
for v in set(a):
    if d[v] % 2 == 0:
        cnt += 1
if cnt % 2 == 1:
    m -= 1
print(m)