n = int(input())
d = {}
for _ in range(n):
    s = input()
    try:
        d[s] += 1
    except Exception:
        d[s] = 1
m = int(input())
for _ in range(m):
    s = input()
    try:
        d[s] -= 1
    except Exception:
        d[s] = -1
ans = 0
for v in d.values():
    ans = max(ans, v)
print(ans)
