import heapq
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
p = list(map(int, input().split()))
l = list(map(int, input().split()))
d = list(map(int, input().split()))

ld = []
for i in range(m):
    ld.append([d[i], l[i]])
ld.sort(key=lambda x: (x[1], -x[0]))
ld = deque(ld)

p.sort()
p = deque(p)
ans = 0

cupon_list = []
heapq.heapify(cupon_list)
while len(p) > 0:
    p_i = p.popleft()
    while len(ld) > 0:
        d_i, l_i = ld.popleft()
        if p_i >= l_i:
            heapq.heappush(cupon_list, [-d_i, -l_i])
        else:
            ld.appendleft([d_i, l_i])
            break
    # 候補の中から割引額が最大のものを選ぶ
    l_i = 0
    d_i = 0
    # print(p_i, cupon_list)
    if len(cupon_list) > 0:
        while len(cupon_list) > 0:
            tmp_d_i, tmp_l_i = heapq.heappop(cupon_list)
            tmp_d_i = -tmp_d_i
            tmp_l_i = -tmp_l_i
            if p_i >= tmp_l_i:
                d_i = tmp_d_i
                l_i = tmp_l_i
                break
    # print(ans, p_i, d_i, l_i, p_i - d_i)
    ans += p_i - d_i
print(ans)
