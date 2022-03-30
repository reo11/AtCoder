import sys
input = sys.stdin.readline
n = int(input())
s = list(str(input().rstrip()))
q = int(input())


class SSQ:
    def __init__(self, n, e):
        # 単位元
        self.e = e
        # num_min:n以上の最小の2のべき乗
        self.num_min = 2**(n-1).bit_length()
        self.seg_min = [self.e]*2*self.num_min

    def update(self, k, x):
        k += self.num_min-1
        self.seg_min[k] = x
        while k:
            k = (k-1)//2
            self.seg_min[k] = self.seg_min[k*2+1] or self.seg_min[k*2+2]

    def query(self, p, q):
        q += 1
        if q <= p:
            return self.e
        p += self.num_min-1
        q += self.num_min-2
        res = self.e
        while q-p > 1:
            if p & 1 == 0:
                res = res or self.seg_min[p]
            if q & 1 == 1:
                res = res or self.seg_min[q]
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = res or self.seg_min[p]
        else:
            res = res or self.seg_min[p] or self.seg_min[q]
        return res

ssqs = [SSQ(n, False) for i in range(26)]

for i in range(n):
    ssqs[ord(s[i]) - ord('a')].update(i, True)

out = []
for i in range(q):
    com, x, y = list(input().split())
    if com == '1':
        idx = int(x) - 1
        pre_alph = ord(s[idx]) - ord('a')
        ssqs[pre_alph].update(idx, False)
        s[idx] = y
        alph = ord(y) - ord('a')
        ssqs[alph].update(idx, True)
    else:
        x, y = int(x) - 1, int(y) - 1
        cnt = 0
        for i in range(26):
            cnt += 1 if ssqs[i].query(x, y) else 0
        out.append(str(cnt))
print("\n".join(out))
