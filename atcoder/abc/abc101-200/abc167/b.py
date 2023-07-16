a, b, c, k = map(int, input().split())

ans = 0
if a >= k:
    ans += k
else:
    ans += a
    k -= a
    if b >= k:
        pass
    else:
        k -= b
        ans -= k
print(ans)
