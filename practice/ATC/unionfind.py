class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x_root = self.Find_Root(x)
        y_root = self.Find_Root(y)

        if(x_root == y_root):
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x_root] >= self.rank[y_root]:
            self.root[x_root] += self.root[y_root]
            self.root[y_root] = x_root
        else:
            self.root[y_root] += self.root[x_root]
            self.root[x_root] = y_root

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return self.root[self.Find_Root(x)]


n, q = map(int, input().split())
uf = UnionFind(n)
ans = []
for i in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        uf.Unite(a, b)
    if p == 1:
        if uf.isSameGroup(a, b):
            ans.append("Yes")
        else:
            ans.append("No")
print("\n".join(ans))
