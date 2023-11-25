import heapq
from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
ix = []

for _ in range(q):
    i, x = map(int, input().split())
    ix.append((i, x))

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

multiset = MultiSet()
for ai in a:
    multiset.add(ai)

mex_candidates = []
for i in range(2 * n + 1):
    if multiset.include(i):
        continue
    else:
        mex_candidates.append(i)
heapq.heapify(mex_candidates)

ans = []
for i, x in ix:
    ai = a[i - 1]
    heapq.heappush(mex_candidates, ai)
    multiset.erase(ai)
    multiset.add(x)
    a[i - 1] = x

    while multiset.include(mex_candidates[0]):
        heapq.heappop(mex_candidates)
    ans.append(mex_candidates[0])
print(*ans, sep="\n")
