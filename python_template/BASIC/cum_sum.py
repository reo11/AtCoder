# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


class OneDimSum:
    def __init__(self, a):
        self.s = [0]
        for v in range(a):
            self.s.append(self.s[-1] + v)

    def solve(self, left, right):
        # 1-indexed
        return self.s[right] - self.s[left - 1]
