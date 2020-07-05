import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
edges = []
ans = 0
for _ in range(n-1):
   u, v = map(int, input().split())
   edges.append([min(u, v), max(u, v)])

for l in range(1, n+1):
   ans += (n - l + 1) * (n - l + 2) // 2

for l, r in edges:
   ans -= (l) * (n - r + 1)
print(ans)
