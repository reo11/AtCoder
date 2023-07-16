import heapq
from collections import defaultdict


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


if __name__ == "__main__":
    multiset = MultiSet()
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        multiset.add(a)

    max_A = multiset.get_max()
    min_A = multiset.get_min()
    print(f"{max_A} {min_A} {multiset.sum}")
