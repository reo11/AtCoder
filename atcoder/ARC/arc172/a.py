import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
from collections import defaultdict
from bisect import bisect_left

h, w, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

counter = defaultdict(lambda: 0)
candidates = [0]
for i in range(26):
    candidates.append(2**i)
candidates.sort()


def dfs(h, w):
    # h, wの大きさの正方形から作成可能なできるだけ大きい正方形の数
    if h == 1 or w == 1:
        counter[1] += h * w
        return
    min_hw = min(h, w)
    idx = bisect_left(candidates, min_hw)
    size = candidates[idx - 1]

    if size == 0:
        return

    h_cnt = h // size
    w_cnt = w // size
    counter[size] += h_cnt * w_cnt
    # あまり
    mod_h = h % size
    mod_w = w % size
    if mod_h == 0 and mod_w == 0:
        return
    elif mod_h == 0:
        dfs(mod_w, h)
    elif mod_w == 0:
        dfs(mod_h, w)
    else:
        if mod_h < mod_w:
            # あまりが大きい方を大きくする
            dfs(mod_w, h)
            dfs(mod_h, w_cnt * size)
        else:
            dfs(mod_h, w)
            dfs(mod_w, h_cnt * size)

dfs(h, w)
a_count = defaultdict(lambda: 0)
for ai in a:
    a_count[2**ai] += 1

# print(counter)
# print(a_count)

flag = True
for k in reversed(candidates[1:]):
    if counter[k] >= a_count[k]:
        counter[k] -= a_count[k]
        counter[k // 2] += 4 * counter[k]
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")

