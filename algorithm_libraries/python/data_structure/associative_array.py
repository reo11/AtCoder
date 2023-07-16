import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


class AssociativeArray:
    def __init__(self):
        self.d = defaultdict(lambda: 0)

    def get(self, pos):
        return self.d[pos]

    def update(self, pos, value):
        self.d[pos] = value


if __name__ == "__main__":
    q = int(input())
    aa = AssociativeArray()
    queries = []
    ans = []
    for _ in [0] * q:
        q_i = input().split()
        queries.append(q_i)
    for q_i in queries:
        if q_i[0] == "0":
            pos, value = q_i[1:]
            aa.update(pos, value)
        else:
            pos = q_i[1]
            ans.append(aa.get(pos))
    print(*ans, sep="\n")
