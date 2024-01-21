from collections import defaultdict

nexts = defaultdict(lambda: -1)
n = int(input())
a = list(map(int, input().split()))
ans = []

for i, ai in enumerate(a):
    if ai == -1:
        ans.append(i + 1)
    else:
        nexts[ai] = i + 1

while len(ans) < n:
    ans.append(nexts[ans[-1]])
print(*ans, sep=" ")