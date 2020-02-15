import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
out = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt_unk = 0
    l = -1
    for v in a:
        if v == -1:
            cnt_unk += 1
        else:
            if l == -1:
                l = v
            r = v
    # all -1
    if cnt_unk == n:
        out.append("0 0")
        continue

    d = deque(a)
    d.appendleft(l)
    d.append(r)

    min_ = 10 ** 10
    max_ = 0
    for i in range(1, len(d)-1):
        if d[i] == -1:
            for v in [d[i-1], d[i+1]]:
                if v != -1:
                    max_ = max(max_, v)
                    min_ = min(min_, v)

    res = (max_ + min_) // 2
    for i in range(1, len(d)-1):
        if d[i] == -1:
            d[i] = res

    ans = [0, res]
    for i in range(len(d)-1):
        sa = abs(d[i] - d[i+1])
        if sa > ans[0]:
            ans[0] = sa
    out.append("{} {}".format(ans[0], ans[1]))

print("\n".join(out))