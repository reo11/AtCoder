n, p, q = map(int, input().split())
d = list(map(int, input().split()))

ans = float("inf")

# Pで買っても良い
# Qで買っても良い
min_d = min(d)
ans = min(min_d + q, p)
print(ans)
