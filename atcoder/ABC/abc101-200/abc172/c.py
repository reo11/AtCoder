import bisect
import sys

input = sys.stdin.readline


def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


n, m, k = map(int, input().split())
a = cumsum(list(map(int, input().split())))
b = cumsum(list(map(int, input().split())))

ans = 0
for a_num, v in enumerate(a):
    tmp = 0
    if k >= v:
        b_num = bisect.bisect_right(b, k - v) - 1
        tmp = a_num + b_num
    ans = max(ans, tmp)
print(ans)
