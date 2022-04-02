import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
n = int(input())
a = []
b = []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

a.sort()
b.sort()
if n % 2 == 0:
    ans = 0
    i = n // 2 - 1
    j = n // 2
    tmp = [[a[i], b[i]], [a[j], b[j]]]
    ans = (b[i] + b[j]) - (a[i] + a[j]) + 1
    print(ans)
else:
    mid_l = a[n // 2]
    mid_r = b[n // 2]
    print(mid_r - mid_l + 1)
