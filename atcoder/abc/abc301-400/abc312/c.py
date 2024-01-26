import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

# 探索していく
x = 1
ans = 0
l = []
for a_i in a:
    l.append(a_i)
for b_i in b:
    l.append(b_i + 1)
l.sort()
for x in l:
    a_count = bisect.bisect_right(a, x)
    b_count = bisect.bisect_left(b, x)
    # print(x, a_count, b_count)
    if a_count >= (m - b_count):
        ans = x
        break
print(ans)
