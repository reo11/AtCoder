from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 2分探索する
ans = []

for i in range(1, n + 1):
    a_idx = bisect_left(a, i)
    ans.append(a[a_idx] - i)

print(*ans, sep="\n")
