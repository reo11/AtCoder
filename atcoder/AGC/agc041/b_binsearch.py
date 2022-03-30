import math
import bisect
n, m, v, p = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

def check(x):
    global n, a, m, v, p
    if x <= p-2:
        return True
    if a[x] + m < a[p-1]:
        return False
    else:
        vote = m * v - m * (p - 1) - m * (n - x - 1) - m
        print(x, vote)
        if vote < 0:
            return True
        else:
            return False

idx = n // 2
step = math.ceil(n / 4)

left = -1
right = n-1
while left + 1 < right:
    x = (left + right) // 2
    if check(x):
        right = x
    else:
        left = x
print(n - right - 1)
l = []
for i in range(n):
    l.append(check(i))
print(l)