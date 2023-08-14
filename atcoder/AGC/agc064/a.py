import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
l = (n * (n + 1)) // 2
counter = defaultdict(lambda: 0)
for i in range(1, n + 1):
    counter[i] = i

ans = []
for i in range(1, n - 1):
    ans.append(i)
ans.append(n)
ans.append(n - 1)
for i in range(1, n + 1):
    counter[i] -= 1
current_v = n
while len(ans) < l:
    for i in range(current_v - 2):
        if counter[current_v] > 0:
            ans.append(current_v)
            counter[current_v] -= 1
        if len(ans) == l:
            break
        if counter[current_v - 1] > 0:
            ans.append(current_v - 1)
            counter[current_v - 1] -= 1
        if len(ans) == l:
            break
    if len(ans) < l and counter[current_v] > 0:
        ans.append(current_v)
        counter[current_v] -= 1
    current_v -= 2


print(*ans, sep=" ")


