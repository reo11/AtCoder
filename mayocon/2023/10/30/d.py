import sys
import bisect
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = float("inf")


w, h = map(int, input().split())
n = int(input())
p = []
q = []

for _ in range(n):
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)

a_size = int(input())
x = list(map(int, input().split()))
b_size = int(input())
y = list(map(int, input().split()))
x.sort()
y.sort()

# hash_mapで管理する
# 最後にhash_mapの個数を見れば0があるかどうかわかる
# minは0かhash_mapのmin、maxはhash_mapのmax

hash_map = defaultdict(lambda: 0)
for i in range(n):
    pi, qi = p[i], q[i]
    # 左上をそのエリアの識別座標とする
    x_idx = bisect.bisect_left(x, pi)
    y_idx = bisect.bisect_left(y, qi)
    hash_map[f"{x_idx}_{y_idx}"] += 1

# [min, max]
ans = [INF, -INF]

for k, v in hash_map.items():
    ans[0] = min(ans[0], v)
    ans[1] = max(ans[1], v)

if len(hash_map.keys()) < (a_size + 1) * (b_size + 1):
    ans[0] = 0

print(*ans, sep=" ")