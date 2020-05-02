from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m, q = map(int, input().split())
abcd = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    abcd.append([a-1, b-1, c, d])

def dfs(A, depth, max_a):
    if depth == n:
        score = 0
        for a, b, c, d in abcd:
            if A[b] - A[a] == c:
                score += d
        return score
    ans = 0
    for i in range(max_a, m+1):
        ans = max(ans, dfs(A + [i], depth+1, i))
    return ans

ans = dfs([1], 1, 1)
print(ans)

