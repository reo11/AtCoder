class UnionFind():
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
        return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] > self.table[s2]:
                self.table[s2] = s1
                self.table[s1] -= 1
                self.size[s1] += self.size[s2]
                self.size[s2] = 0
            else:
                self.table[s1] = s2
                self.table[s2] -= 1
                self.size[s2] += self.size[s1]
                self.size[s1] = 0
        return

n = int(input())
u = [0] * (n-1)
v = [0] * (n-1)
w = [0] * (n-1)
uf = UnionFind(n)

for i in range(n-1):
    u[i], v[i], w[i] = map(int, input().split())
    u[i] -= 1
    v[i] -= 1
    w[i] = w[i] % 2
    # 同じなら0、違ったら1
    if w[i] == 0:
        uf.union(u[i], v[i])

group1 = []
group2 = []

for i in range(n-1):
    if w[i] == 1:
        if uf.find(u[i]) in group1:
            group2.append(v[i])
        elif uf.find(u[i]) in group2:
            group1.append(v[i])
        elif uf.find(v[i]) in group1:
            group2.append(u[i])
        elif uf.find(v[i]) in group2:
            group1.append(u[i])
        else:
            group1.append(v[i])
            group2.append(u[i])

for i in range(n):
    if uf.find(i) in group1:
        print(0)
    else:
        print(1)
