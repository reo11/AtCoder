from collections import defaultdict
n, w = map(int, input().split())
stp = []
for _ in range(n):
    s, t, p = map(int, input().split())
    stp.append((s, t, p))

imos = defaultdict(lambda: [])
for s, t, p in stp:
    imos[s].append(p)
    imos[t].append(-p)

flag = True
value = 0
for time, v in sorted(imos.items(), key=lambda x: x[0]):
    for p in v:
        value += p
    # print(time, value)
    if value > w:
        flag = False
        break
print("Yes" if flag else "No")
