# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B
import sys

input = sys.stdin.readline

n, q = map(int, input().split())


class RMQ:
    def __init__(self, n, e):
        # 単位元
        self.e = e
        # num_min:n以上の最小の2のべき乗
        self.num_min = 2 ** (n - 1).bit_length()
        self.seg = [self.e] * 2 * self.num_min

    def initialize(self, init):
        # 初期値が指定されている場合
        # set_val
        for i in range(n):
            self.seg[i + self.num_min - 1] = init[i]
        # built
        for i in range(self.num_min - 2, -1, -1):
            self.seg[i] = min(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num_min - 1
        self.seg[k] += x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.seg[k * 2 + 1] + self.seg[k * 2 + 2]

    def query(self, p, q):
        q += 1
        if q <= p:
            return self.e
        p += self.num_min - 1
        q += self.num_min - 2
        res = self.e
        while q - p > 1:
            if p & 1 == 0:
                res += self.seg[p]
            if q & 1 == 1:
                res += self.seg[q]
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res += self.seg[p]
        else:
            res += self.seg[p] + self.seg[q]
        return res


e = 0
rmq = RMQ(n, e)

for _ in range(q):
    com, x, y = map(int, input().split())
    x -= 1
    if com == 0:
        rmq.update(x, y)
    else:
        y -= 1
        ans = rmq.query(x, y)
        print(ans)
