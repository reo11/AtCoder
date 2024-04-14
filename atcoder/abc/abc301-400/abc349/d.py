import sys
import pypyjit
import math
from collections import deque
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

l, r = map(int, input().split())

def max_x(l, r):
    diff = r - l
    if diff == 0:
        return None

    for x in range(math.ceil(math.log2(diff)) + 1, -1, -1):
        if 2 ** x > diff:
            continue

        # l以上でxの倍数である最小値を求める
        if l % (2 ** x) == 0:
            new_l = l
        else:
            new_l = l + (2 ** x - (l % (2 ** x)))
        new_r = new_l + 2 ** x
        if new_r > r:
            continue
        else:
            result = []
            left = max_x(l, new_l)
            if left is not None:
                for lr in max_x(l, new_l):
                    result.append(lr)
            result.append([new_l, new_r])
            right = max_x(new_r, r)
            if right is not None:
                for lr in max_x(new_r, r):
                    result.append(lr)
            return result

candidates = deque()
q = [[l, r]]

while q:
    li, ri = q.pop()
    diff = ri - li
    if diff == 1:
        candidates.append([li, ri])
        continue
    elif diff == 0:
        continue

    for x in range(math.ceil(math.log2(diff)) + 1, -1, -1):
        if 2 ** x > diff:
            continue

        # l以上でxの倍数である最小値を求める
        if li % (2 ** x) == 0:
            new_l = li
        else:
            new_l = li + (2 ** x - (li % (2 ** x)))
        new_r = new_l + 2 ** x
        if new_r > ri:
            continue
        else:
            candidates.append([new_l, new_r])
            q.append([li, new_l])
            q.append([new_r, ri])
            break



ans = []
ans.append(str(len(candidates)))
for l, r in sorted(candidates):
    ans.append(f"{l} {r}")

print("\n".join(ans))