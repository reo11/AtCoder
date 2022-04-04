n, k = map(int, input().split())
ab = {}
for i in range(n):
    a, b = map(int, input().split())
    try:
        ab[a] += b
    except Exception:
        ab[a] = b
count = 0
ans = 0
for key in sorted(ab.keys()):
    count += ab[key]
    if count >= k:
        ans = key
        break
print(ans)
