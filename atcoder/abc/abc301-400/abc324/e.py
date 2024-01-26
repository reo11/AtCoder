import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, t = input().split()
t = list(t)
n = int(n)
s = [list(input()) for _ in range(n)]

# よく知らんが分割統治的なやつ
# si + sjにtが部分列として含まれるようにする
# それぞれのsにtの部分文字列の判定をして、計上しておく
counter = defaultdict(int)
rev_counter = defaultdict(int)

for idx, si in enumerate(s):
    # 順方向
    queue_t_idx = 0
    cnt = 1
    # counter[0] += 1
    for ij in range(len(si)):
        sij = si[ij]
        if queue_t_idx > len(t) - 1:
            break
        if sij == t[queue_t_idx]:
            queue_t_idx += 1
            cnt += 1
    max_num = cnt - 1
    counter[max_num] += 1
    # 逆方向
    queue_t_idx = len(t) - 1
    cnt = 1
    rev_counter[0] += 1
    for ij in reversed(range(len(si))):
        sij = si[ij]
        if queue_t_idx < 0:
            break
        if sij == t[queue_t_idx]:
            rev_counter[cnt] += 1
            queue_t_idx -= 1
            cnt += 1

# 分割位置を全探索
ans = 0
for i in range(len(t) + 1):
    ans += counter[i] * rev_counter[len(t) - i]

print(ans)
