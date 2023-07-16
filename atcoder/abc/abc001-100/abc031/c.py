n = int(input())
a = list(map(int, input().split()))

takahashi = -1000000000

for i in range(n):
    aoki = -1000000000
    ans_ij = None
    for j in range(n)[::-1]:
        if i == j:
            continue
        aoki_score = 0
        for idx, k in enumerate(range(min(i, j), max(i, j) + 1)):
            if idx % 2 == 1:
                aoki_score += a[k]
        if aoki_score >= aoki:
            aoki = aoki_score
            ans_ij = [i, j]
    if ans_ij:
        i, j = ans_ij
        t = 0
        for idx, v in enumerate(range(min(i, j), max(i, j) + 1)):
            if idx % 2 == 0:
                t += a[v]
        takahashi = max(takahashi, t)

print(takahashi)
