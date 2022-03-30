import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

MAX = 1000001
dp = [True for _ in range(MAX)]
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
a = sorted(list(set(a)))
ans = 0
for v in a:
   if cnt[v] <= 1 and dp[v]:
      ans += 1
   m = v
   while m < MAX:
      dp[m] = False
      m += v
print(ans)