import sys

input = sys.stdin.readline
n = int(input())
color = [0] * (10**6 + 2)
for i in range(n):
    a, b = map(int, input().split())
    color[a] += 1
    color[b + 1] -= 1

ans = 0
v = 0
for i in range(len(color)):
    v += color[i]
    ans = max(ans, v)
print(ans)
