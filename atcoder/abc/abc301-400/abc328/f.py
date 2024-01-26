from collections import defaultdict

INF = float("inf")


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
            return -INF  # コスト算出不可
        return self.weight[x] - self.weight[y]


n, q = map(int, input().split())
abd = []

uf = WeightedUnionFind(n)
for _ in range(q):
    a, b, d = map(int, input().split())
    abd.append((a, b, d))

ans = []
x = defaultdict(int)
# グラフを作っていく
for i in range(q):
    a, b, d = abd[i]
    if a == b:
        if d == 0:
            ans.append(i + 1)
        continue
    if uf.diff(a, b) == -INF:
        # 繋げる
        uf.union(a, b, d)
        ans.append(i + 1)
        continue
    elif uf.diff(a, b) == d:
        # すでに繋がっていて、コストが一致している
        ans.append(i + 1)
        uf.union(a, b, d)
        continue

print(*ans, sep=" ")
