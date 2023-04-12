from collections import defaultdict

n = int(input())
ans = 0

d = defaultdict(int)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a * b > n:
            break
        d[a * b] += 1

for k_i in d.keys():
    k_j = n - k_i
    if k_j not in d:
        continue
    else:
        ans += d[k_i] * d[k_j]
print(ans)

