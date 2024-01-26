from math import ceil

n = int(input())
a = list(map(int, input().split()))

ans = 10**10

m1 = a[int(n / 2)]
m2 = int(sum(a) / n)
m3 = ceil(sum(a) / n)

for v in [m1, m2, m3]:
    cost = 0
    for i in range(n):
        cost += (a[i] - v) ** 2
    ans = min(cost, ans)
print(ans)
