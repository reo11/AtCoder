import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
s = [[i for i in list(str(input()))] for _ in range(h)]

class UnionFind():
    def __init__(self, n):
        self.n = n + 1
        self.parents = [-1] * (n + 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

pos_num = defaultdict(lambda: len(pos_num))
visited = [[False] * w for _ in range(h)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_magnet_neighbour(y, x):
    for dy, dx in dxy:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == "#":
            return True
    return False

ans = 0
q = deque()
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            visited[i][j] = True
            continue
        elif visited[i][j]:
            continue
        else:
            q = deque([(i, j)])
            visit_path = set([(i, j)])
            if not is_magnet_neighbour(i, j):
                while q:
                    y, x = q.popleft()
                    visited[y][x] = True
                    for dy, dx in dxy:
                        ny = y + dy
                        nx = x + dx
                        if not(0 <= ny < h and 0 <= nx < w):
                            continue
                        if s[ny][nx] == "#":
                            continue
                        if (ny, nx) in visit_path:
                            continue
                        visit_path.add((ny, nx))
                        if is_magnet_neighbour(ny, nx):
                            continue
                        q.append((ny, nx))
            ans = max(ans, len(visit_path))
print(ans)
