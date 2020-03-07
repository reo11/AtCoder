n, a, b = map(int, input().split())
tmp = n // (a + b)
ans = tmp * a + min(n - tmp * (a + b), a)
print(ans)