import sys
from collections import defaultdict

sys.setrecursionlimit(20000000)
connection = defaultdict(lambda: [])

n = int(input())

ab = []
for i in range(n - 1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
    ab.append((a, b))

c = list(map(int, input().split()))
c.sort()

ans = [0] * (n + 1)

checked_list = []


def dfs(num):
    checked_list.append(num)
    ans[num] = c.pop()
    for next_num in connection[num]:
        if next_num not in checked_list:
            dfs(next_num)


l = []
for i in range(1, n + 1):
    l.append([i, len(connection[i])])
l.sort(key=lambda x: x[1], reverse=True)
dfs(l[0][0])

score = 0

for a, b in ab:
    score += min(ans[a], ans[b])

print(score)
print(" ".join(map(str, ans[1:])))
