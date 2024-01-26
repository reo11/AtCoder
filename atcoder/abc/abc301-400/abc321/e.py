import math
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

t = int(input())
ans = []
for ti in range(t):
    # 完全二分木
    n, x, k = map(int, input().split())
    if k == 0:
        ans.append(1)
        continue
    elif k > 3 * math.log2(n):
        ans.append(0)
        continue
    ansi = 0
    # xの子孫を数える
    base = x * (2**k)
    if base <= n:
        ansi += min(n, (base + (2**k) - 1)) - base + 1
    que = deque([])
    if x // 2 > 0:
        que = deque([[x, x // 2, k - 1]])
    # xの祖先を数える
    while que:
        # print(ti, que, ansi)
        x, parent, k = que.popleft()
        if k == 0:
            # 親を数えて終わり
            ansi += 1
            break
        else:
            if x % 2 == 0:
                other_x = x + 1
            else:
                other_x = x - 1
            base = other_x * (2 ** (k - 1))
            if base <= n:
                ansi += min(n, (base + (2 ** (k - 1)) - 1)) - base + 1
            if parent // 2 > 0:
                que.append([parent, parent // 2, k - 1])
    ans.append(ansi)
print(*ans, sep="\n")
