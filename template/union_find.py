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
            self.rank[x_root] += self.rank[y_root]
            self.root[y_root] = x_root
        else:
            self.rank[y_root] += self.rank[x_root]
            self.root[x_root] = y_root

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return self.rank[self.Find_Root(x)]
