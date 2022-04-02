# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
import sys

input = sys.stdin.readline

n, q = map(int, input().split())


class RMQ:
    def __init__(self, n, e):
        # 単位元
        self.e = e
        # num_min:n以上の最小の2のべき乗
        self.num_min = 2 ** (n - 1).bit_length()
        self.seg_min = [self.e] * 2 * self.num_min

    def init_min(self, init_min_val):
        # 初期値が指定されている場合
        # set_val
        for i in range(n):
            self.seg_min[i + self.num_min - 1] = init_min_val[i]
        # built
        for i in range(self.num_min - 2, -1, -1):
            self.seg_min[i] = min(self.seg_min[2 * i + 1], self.seg_min[2 * i + 2])

    def update_min(self, k, x):
        k += self.num_min - 1
        self.seg_min[k] = x
        while k:
            k = (k - 1) // 2
            self.seg_min[k] = min(self.seg_min[k * 2 + 1], self.seg_min[k * 2 + 2])

    def query_min(self, p, q):
        q += 1
        if q <= p:
            return self.e
        p += self.num_min - 1
        q += self.num_min - 2
        res = self.e
        while q - p > 1:
            if p & 1 == 0:
                res = min(res, self.seg_min[p])
            if q & 1 == 1:
                res = min(res, self.seg_min[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = min(res, self.seg_min[p])
        else:
            res = min(min(res, self.seg_min[p]), self.seg_min[q])
        return res


e = (2 ** 31) - 1
rmq = RMQ(n, e)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        rmq.update_min(x, y)
    else:
        ans = rmq.query_min(x, y)
        print(ans)
