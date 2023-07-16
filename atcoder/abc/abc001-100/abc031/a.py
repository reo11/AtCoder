a, d = map(int, input().split())

m = a * d
print(max(m + a, m + d))
