n, w = map(int, input().split())
vw = [input().split() for _ in range(n)]
vw = [(int(x[0]), int(x[1])) for x in vw]

pdp = [0 for _ in range(w + 1)]
cdp = [0 for _ in range(w + 1)]

for i in range(n):
    for j in range(w):
        if j + vw[i][1] < w + 1:
            cdp[j + vw[i][1]] = max(pdp[j + vw[i][1]], pdp[j] + vw[i][0])
    pdp = cdp[:]
print(max(cdp))
