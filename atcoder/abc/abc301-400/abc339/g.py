from bisect import bisect
from heapq import merge

class MergeSortTree:
    def __init__(self, N, A):
        self.tree_size = 2**(N-1).bit_length()
        self.tree = [None]*(2*self.tree_size)
        for i, a in enumerate(A):
            self.tree[self.tree_size-1+i] = [a]
        for i in range(N, self.tree_size):
            self.tree[self.tree_size-1+i] = []
        for i in range(self.tree_size-2, -1, -1):
            *self.tree[i], = merge(self.tree[2*i+1], self.tree[2*i+2])

    # count elements A_i s.t. A_i <= k for i in [l, r)
    def query1(self, l, r, k):
        L = l + self.tree_size
        R = r + self.tree_size
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                s += bisect(self.tree[R-1], k-1)
            if L & 1:
                s += bisect(self.tree[L-1], k-1)
                L += 1
            L >>= 1; R >>= 1
        return s

    # count elements A_i s.t. a <= A_i < b for i in [l, r)
    def query(self, l, r, a, b):
        L = l + self.tree_size
        R = r + self.tree_size
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                s += bisect(self.tree[R-1], b-1) - bisect(self.tree[R-1], a-1)
            if L & 1:
                s += bisect(self.tree[L-1], b-1) - bisect(self.tree[L-1], a-1)
                L += 1
            L >>= 1; R >>= 1
        return s

n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    alpha, beta, gamma = map(int, input().split())
    queries.append((alpha, beta, gamma))

def decode(alpha, beta, gamma, pre_b):
    l = alpha ^ pre_b
    r = beta ^ pre_b
    x = gamma ^ pre_b
    return l, r, x



ans = []
pre_b = 0
for query in queries:
    alpha, beta, gamma = query
    l, r, x = decode(alpha, beta, gamma, pre_b)
    ansi = 0
    for i in range(l - 1, r):
        if a[i] <= x:
            ansi += a[i]
    ans.append(ansi)
    pre_b = ansi
print(*ans, sep='\n')