n, m = map(int, input().split())

ans = (m * 1900 + (n - m) * 100) * 2**m
print(ans)
