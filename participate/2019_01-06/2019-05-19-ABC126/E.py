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

n, m = map(int, input().split())

x = [0] * m
y = [0] * m
z = [0] * m



