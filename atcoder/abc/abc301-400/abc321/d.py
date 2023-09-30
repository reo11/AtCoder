from bisect import bisect_left, bisect_right

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

# 二部探索をする
a = sorted(a)
b = sorted(b)
# 累積和をとる
cumsum_b = cumsum(b)

ans = 0
for ai in a:
    # 二部探索で価格がPになる境界を探す
    # つまり P - ai <= bj となる最小のjを探す
    j = bisect_left(b, p - ai)
    ans += cumsum_b[j]
    ans += ai * j
    ans += (m - j) * p
print(ans)
