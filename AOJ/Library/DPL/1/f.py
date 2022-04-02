n, w = map(int, input().split())
vw = [input().split() for _ in range(n)]
vw = [(int(x[0]), int(x[1])) for x in vw]
v_max = sum([x[0] for x in vw])

INF = 10 ** 9 + 1
pdp = [INF for _ in range(v_max + 1)]
cdp = [INF for _ in range(v_max + 1)]
pdp[0] = 0
cdp[0] = 0

for i in range(n):
    for j in range(v_max + 1):
        if j + vw[i][0] < v_max + 1:
            cdp[j + vw[i][0]] = min(pdp[j + vw[i][0]], pdp[j] + vw[i][1])
        else:
            break
    pdp = cdp[:]

ans = INF
for i in range(len(cdp)):
    if cdp[i] <= w:
        ans = i

print(ans)
