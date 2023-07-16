k, n = map(int, input().split())
a = list(map(int, input().split()))
dist = []

for i in range(n - 1):
    dist.append(abs(a[i + 1] - a[i]))
dist.append(abs(k - a[-1] + a[0]))

print(sum(dist) - max(dist))
