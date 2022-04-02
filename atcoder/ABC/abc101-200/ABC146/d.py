import sys

sys.setrecursionlimit(500000)

N = int(input())
E = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    E[a].append((b, i))
    E[b].append((a, i))
K = max(len(e) for e in E)
print(K)

ans = [-1] * (N - 1)


def dfs(v=1, p=0, p_col=-1):
    col = 1
    for u, idx in E[v]:
        if u != p:
            if col == p_col:
                col += 1
            ans[idx] = col
            dfs(u, v, col)
            col += 1


dfs()
print("\n".join(map(str, ans)))
