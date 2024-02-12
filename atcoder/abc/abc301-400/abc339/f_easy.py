from collections import defaultdict

n = int(input())
a = [int(input()) for _ in range(n)]

counter = defaultdict(int)
for ai in a:
    counter[ai] += 1

ans = 0
for i in range(n):
    for j in range(i, n):
        aij = a[i] * a[j]
        if aij in counter:
            if i == j:
                ans += counter[aij]
            else:
                ans += counter[aij] * 2
print(ans)