a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

cost = a * s + t * b
if s + t >= k:
    cost -= c * (s + t)
print(cost)
