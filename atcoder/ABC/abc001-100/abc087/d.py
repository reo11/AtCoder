def main():
    n, m = map(int, input().split())
    g = [[] for i in range(n)]
    for i in range(m):
        l, r, d = map(int, input().split())
        g[l - 1].append((r - 1, d))
        g[r - 1].append((l - 1, -d))
    dis = [0] * n
    visited = [False] * n
    stack = list(range(n))
    while len(stack):
        v = stack[-1]
        stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        for u, d in g[v]:
            if not visited[u]:
                dis[u] = dis[v] + d
                stack.append(u)
    for v in range(n):
        for u, d in g[v]:
            if dis[v] + d != dis[u]:
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    main()
