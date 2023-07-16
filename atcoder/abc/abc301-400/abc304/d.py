import bisect
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

w, h = map(int, input().split())
n = int(input())
pq = []
for _ in range(n):
    p, q = map(int, input().split())
    pq.append([p, q])
a_num = int(input())
a = list(map(int, input().split()))
b_num = int(input())
b = list(map(int, input().split()))

# 座標圧縮してdictで個数を管理して、最後に数える
# 座標xを入れたらそのxが圧縮後に何番になるかを返す
sorted_x = sorted(a)
sorted_y = sorted(b)
px = [bisect.bisect_left(sorted_x, x) for x, _y in pq]
qx = [bisect.bisect_left(sorted_y, y) for _x, y in pq]
new_pq = list(zip(px, qx))

ans_min = 0
ans_max = 0
counter = defaultdict(int)
for p, q in new_pq:
    counter[f"{p}_{q}"] += 1
ans_list = list(counter.values())

if len(ans_list) < (a_num + 1) * (b_num + 1):
    ans_min = 0
else:
    ans_min = min(ans_list)
ans_max = max(ans_list)
print(f"{ans_min} {ans_max}")
