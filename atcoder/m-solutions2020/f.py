import sys
from collections import defaultdict

input = sys.stdin.readline

INF = 10 ** 12
n = int(input())

xyu = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: set())))
siki = defaultdict(lambda: defaultdict(lambda: []))
min_clash = INF
for _ in range(n):
    x, y, u = input().split()
    x = int(x)
    y = int(y)
    xyu[u]["x"][x].add(y)
    xyu[u]["y"][y].add(x)
    siki[u].append([1, y - x])
    siki[u].append([-1, y + x])

# 横向きチェック
for y, lxs in xyu["L"]["y"].items():
    if len(xyu["R"]["y"][y]) > 0:
        for r in xyu["R"]["y"][y]:
            for l_ in lxs:
                if l_ > r:
                    min_clash = min(min_clash, abs(l_ - r) * 5)
# 縦向きチェック
for x, lxs in xyu["U"]["x"].items():
    if len(xyu["D"]["x"][x]) > 0:
        for d in xyu["D"]["x"][x]:
            for u in lxs:
                if d > u:
                    min_clash = min(min_clash, abs(u - d) * 5)

# 交差チェック
# 一次関数にしてその係数で接触するか判断できる
# for s in siki["U"]:
#     if s in siki["L"]:

#     if s in siki["R"]:


# if min_clash == INF:
#     print("SAFE")
# else:
#     print(min_clash)
