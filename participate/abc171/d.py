import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

d = defaultdict(lambda: 0)
ans = 0
for v in a:
   d[v] += 1
   ans += v
for i in range(q):
   b, c = bc[i]
   if b > c:
      ans -= (b - c) * d[b]
   else:
      ans += (c - b) * d[b]
   d[c] += d[b]
   d[b] = 0
   print(ans)
