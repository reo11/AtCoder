n, k = map(int, input().split())
tmp1 = n % k
tmp2 = max(k, tmp1) - min(k, tmp1)
ans = min(tmp2, k - tmp2)
print(ans)
