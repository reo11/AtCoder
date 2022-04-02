from collections import defaultdict

d = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))

for v in a:
    d[v - 1] += 1

ans = []
for i in range(n):
    ans.append(str(d[i]))
print("\n".join(ans))
