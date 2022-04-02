import sys
from collections import defaultdict
from math import ceil

input = lambda: sys.stdin.readline().rstrip()

INF = 2 ** 50
n = int(input())
a = list(map(int, input().split()))
if n == 0 and a[0] == 0:
    print(-1)
    exit()
# その層で作ることができるノードの最大値
max_i = defaultdict(lambda: INF)
max_i[0] = 1

for i in range(1, n + 1):
    if max_i[i - 1] * 2 - a[i] < INF:
        max_i[i] = max_i[i - 1] * 2 - a[i]
    else:
        break
for i in max_i.keys():
    if i == 0:
        continue
    max_i[i] += a[i]

a = a[::-1]
cnt = 0
# 下の層の頂点の数
pre_cnt = 0
for i, v in enumerate(a):
    idx = n - i
    # print(idx, list(max_i.items()))
    if idx in max_i.keys():
        if v + ceil((pre_cnt) / 2) > max_i[idx]:
            print(-1)
            exit()
        # 上の頂点数
        pre_cnt = min(v + pre_cnt, max_i[idx])
        cnt += pre_cnt
    else:
        if v + ceil((pre_cnt) / 2) > INF:
            print(-1)
            exit()
        # 上の頂点数
        pre_cnt = min(v + pre_cnt, INF)
        cnt += pre_cnt

print(cnt)
