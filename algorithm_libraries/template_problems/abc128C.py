n, m = map(int, input().split())
ss = []
for _ in range(m):
    k, *s = list(map(int, input().split()))
    s_set = set(s)
    ss.append(s_set)
p = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    f = True
    for k in range(m):
        cnt = 0
        for j in range(n):
            if (i >> j) & 1 and j + 1 in ss[k]:
                cnt += 1
        if cnt % 2 != p[k]:
            f = False
    if f:
        ans += 1
print(ans)
