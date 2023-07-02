import heapq
import sys
from collections import defaultdict
from typing import List
import sys
input = lambda: sys.stdin.readline().rstrip()

class MultiSet:
    def __init__(self) -> None:
        self.cnt_dict = defaultdict(int)
        self.rank_min = []
        self.rank_max = []
        self.size = 0
        self.sum = 0

    def add(self, num: int) -> None:
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = cnt + 1

        heapq.heappush(self.rank_min, num)
        heapq.heappush(self.rank_max, -num)
        self.size += 1
        self.sum += num

    def erase(self, num: int, d: int = 1) -> None:
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = max(cnt - d, 0)
        self.size -= d
        self.sum -= num * d

    def get_max(self) -> int:
        while self.cnt_dict[-self.rank_max[0]] == 0:
            -heapq.heappop(self.rank_max)
        return -self.rank_max[0]

    def get_min(self) -> int:
        while self.cnt_dict[self.rank_min[0]] == 0:
            heapq.heappop(self.rank_min)
        return self.rank_min[0]

    def include(self, num: int) -> bool:
        return self.cnt_dict.get(num, 0) > 0

class Solver:
    def __init__(self, A: List[int], k: int) -> None:
        self.A = A
        self.X = MultiSet()
        self.Y = MultiSet()
        self.sum_x = 0
        self.k = k
        self.use_y = len(A) > k
        for i in range(k):
            self.X.add(A[i])
        for i in range(k, len(A)):
            self.Y.add(A[i])

    def balance(self) -> None:
        if self.Y.size == 0:
            return
        elif self.X.size == 0:
            self.X.add(self.Y.get_max())
            self.Y.erase(self.Y.get_max())
        else:
            while self.X.size < self.k or self.X.get_min() < self.Y.get_max():
                if self.X.size < self.k:
                    self.X.add(self.Y.get_max())
                    self.Y.erase(self.Y.get_max())
                else:
                    tmp_x = self.X.get_min()
                    tmp_y = self.Y.get_max()
                    self.X.erase(tmp_x)
                    self.Y.erase(tmp_y)
                    self.Y.add(tmp_x)
                    self.X.add(tmp_y)

    def add(self, v: int) -> None:
        if self.use_y:
            self.Y.add(v)
            self.balance()
        else:
            self.X.add(v)

    def erase(self, v: int) -> None:
        if self.X.include(v):
            self.X.erase(v)
        elif self.use_y:
            self.Y.erase(v)
        if self.use_y:
            self.balance()

    def query(self, x: int, y: int) -> int:
        current_y = self.A[x - 1]
        self.A[x - 1] = y
        self.erase(current_y)
        self.add(y)
        return self.X.sum

n, k, q = map(int, input().split())
xy = []
for _ in [0] * q:
    x, y = map(int, input().split())
    xy.append((x, y))

ans = []
solver = Solver(A=[0] * n, k=k)
for x, y in xy:
    ans.append(solver.query(x, y))
print(*ans, sep="\n")
