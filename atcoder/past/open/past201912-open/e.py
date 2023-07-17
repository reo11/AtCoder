from collections import defaultdict

n, q = map(int, input().split())

d = defaultdict(lambda: defaultdict(lambda: False))
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        a = s[1]
        b = s[2]

        d[a][b] = True
    elif s[0] == 2:
        a = s[1]
        for i in range(1, n + 1):
            if i == a:
                continue
            if a in d[i].keys():
                d[a][i] = True
    else:
        a = s[1]
        tmp_keys = list(d[a].keys())
        for follow in tmp_keys:
            for ff in d[follow].keys():
                if ff == a:
                    continue
                d[a][ff] = True

ans = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if i == j:
            fij = "N"
        else:
            fij = "Y" if d[i][j] else "N"
        row.append(fij)
    ans.append("".join(row))
print("\n".join(ans))
