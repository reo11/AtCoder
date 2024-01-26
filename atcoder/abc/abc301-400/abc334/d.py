from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
r = list(map(int, input().split()))
r = sorted(r)
# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


cum_r = cumsum(r)

ans = []
for _ in range(q):
    x = int(input())
    # 二分探索
    ans.append(bisect_right(cum_r, x) - 1)
# print(r, cum_r)
print(*ans, sep="\n")
