from collections import defaultdict
class WeightedUnionFind:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        # 根への距離を管理
        self.weight = [0] * (n + 1)

    # 検索
    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x: int, y: int, w: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x: int, y: int) -> int:
        if self.find(x) != self.find(y):
            return -1  # コスト算出不可
        return self.weight[x] - self.weight[y]

n, q = map(int, input().split())
INF = float("inf")
max_cost_path = defaultdict(lambda: 0)
tree = WeightedUnionFind(n)

cost = 0
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree.union(a, b, c)
    max_cost_path[a] = max(max_cost_path[a], c)
    max_cost_path[b] = max(max_cost_path[b], c)
    cost += c

print(cost)
ans = []
for _ in range(q):
    u, v, w = map(int, input().split())
    tree.union(u, v, w)
    print(u, v, w, max_cost_path)
    if max_cost_path[u] > max_cost_path[v]:
        cost -= max_cost_path[u] - w
        max_cost_path[u] = w
    else:
        cost -= max_cost_path[v] - w
        max_cost_path[v] = w

    ans.append(cost)
print(*ans, sep="\n")
