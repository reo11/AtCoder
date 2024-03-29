from collections import deque


class Dinic:
    # V: 頂点数, E: 辺数
    # O(V^2E)
    def __init__(self, N: int) -> None:
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, fr: int, to: int, cap: int) -> None:
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1: int, v2: int, cap1: int, cap2: int) -> None:
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s: int, t: int) -> bool:
        self.level = level = [None] * self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v: int, t: int, f: int) -> int:
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s: int, t: int) -> int:
        flow = 0
        INF = 10**9 + 7

        while self.bfs(s, t):
            (*self.it,) = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
