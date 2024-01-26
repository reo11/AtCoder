from collections import defaultdict

n, q = map(int, input().split())
tab = []
for i in range(q):
    t, a, b = map(int, input().split())
    tab.append([t, a, b])


follow = defaultdict(lambda: defaultdict(lambda: False))
ans = []
for ti, ai, bi in tab:
    if ti == 1:
        follow[ai][bi] = True
    elif ti == 2:
        follow[ai][bi] = False
    else:
        if follow[ai][bi] and follow[bi][ai]:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans, sep="\n")
