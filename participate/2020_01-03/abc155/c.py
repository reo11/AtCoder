import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
s = [str(input().rstrip()) for _ in range(n)]
c = Counter(s)
d_sorted = sorted(c.items(), key=lambda x:x[1], reverse=True)

m = d_sorted[0][1]
ans = []
for key, v in d_sorted:
    if v == m:
        ans.append(key)
ans.sort()
print("\n".join(ans))
