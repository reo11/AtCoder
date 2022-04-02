import sys
from collections import defaultdict

sys.setrecursionlimit(20000000)
connection = defaultdict(lambda: [])

n = int(input())

ab = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
    ab.append((a, b))

c = list(map(int, input().split()))
c.sort()

ans = [0] * (n + 1)


def dfs(num):
    ans[num] = c.pop()
    for next_num in connection[num]:
        if ans[next_num] == 0:
            dfs(next_num)


dfs(1)

score = 0
for a, b in ab:
    score += min(ans[a], ans[b])

print(score)
print(" ".join(map(str, ans[1:])))
