n, m, k = map(int, input().split())
c = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.size=n
        self.tree = [0] * (n+1)

    def add(self, i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

def InversionNumberByBIT(A):
    ans = 0
    Bit = BIT(max(len(A) + 1, max(A) + 1))
    for i in range(len(A)):
        ans += i - Bit.sum(A[i])
        Bit.add(A[i], 1)
    return ans