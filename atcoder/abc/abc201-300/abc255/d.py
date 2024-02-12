from bisect import bisect_left
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]

a.sort()

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

cumsum_a = cumsum(a)

ans = []
for xi in x:
    ansi = 0
    idx = bisect_left(a, xi)
    # 左は不足、右は過剰
    left_sum = cumsum_a[idx]
    right_sum = cumsum_a[-1] - cumsum_a[idx]
    ansi = (idx * xi - left_sum) + (right_sum - (n - idx) * xi)
    ans.append(ansi)
print(*ans, sep='\n')


