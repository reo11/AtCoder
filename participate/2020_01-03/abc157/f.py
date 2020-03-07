import sys
import bisect

input = sys.stdin.readline
p = 998244353

class FLT:
    def __init__(self, mod=10**9+7):
        self.mod = mod

    def rep_sqr(self, base, k):
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.mod
            base = base * base % self.mod
            k >>= 1
        return ans

    def inv(self, a):
        # 逆元を取る
        return self.rep_sqr(a, self.mod-2)

n = int(input())
flt = FLT(p)
xd = []
xs = []
for i in range(n):
    x, d = map(int, input().split())
    xd.append((x, d))
    xs.append(x)
xd.sort()
xs.sort()

# xds = []
nums = []
for i, (x, d) in enumerate(xd):
    j = bisect.bisect_left(xs, x+d)
    num = j - i - 1
    # xds.append((x, d, num))
    nums.append(num)
print(nums)
tmp_nums = [0 for _ in range(len(nums))]
# 前処理
for i, num in enumerate(nums[::-1]):
    tmp_max = num
    pos = n - i - 1
    if num >= 1:
        for idx, j in enumerate(range(pos + 1, pos + 1 + num)):
            print(idx + 1 + tmp_nums[pos])
            tmp_max = max(tmp_max, idx + 1 + tmp_nums[pos])
    tmp_nums[pos] = tmp_max
print(tmp_nums)

ans = 1
for i, num in enumerate(nums[::-1]):
    ans *= 2
    ans %= p
    if num >= 1:
        ans -= (flt.rep_sqr(2, num) - 1)
        ans %= p
print(ans)
