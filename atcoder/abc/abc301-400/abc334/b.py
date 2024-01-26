INF = 10**19
a, m, l, r = map(int, input().split())
a += INF
a %= m
l += INF
r += INF

l = l + ((a - l) % m)
r = r - ((r - a) % m)

print((r - l) // m + 1)
