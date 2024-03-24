from collections import defaultdict

h, w, m = map(int, input().split())

queries = []

for _ in range(m):
    queries.append(list(map(int, input().split())))

# 逆から辿れば easy win
queries = queries[::-1]

colors = defaultdict(int)

colors[0] = h * w
current_w = w
current_h = h
used_rows = set()
used_cols = set()
for t, a, x in queries:
    if t == 1:
        if a in used_rows:
            continue
        used_rows.add(a)
        colors[x] += current_w
        colors[0] -= current_w
        current_h = max(0, current_h - 1)
    else:
        if a in used_cols:
            continue
        used_cols.add(a)
        colors[x] += current_h
        colors[0] -= current_h
        current_w = max(0, current_w - 1)
    # print(t, a, x, colors, used_rows, used_cols)

ans = []
for k, v in colors.items():
    if v > 0:
        ans.append([k, v])
ans.sort()
ans = [f"{k} {v}" for k, v in ans]
ans = [len(ans)] + ans
print(*ans, sep="\n")