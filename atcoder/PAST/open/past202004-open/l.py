import math

n, k, d = map(int, input().split())
a = list(map(int, input().split()))

# 不可能な場合
if math.ceil(n / d) < k:
    print(-1)
    exit()
else:
    ans = []
    for i in range(k):
        ans.append(a[i * d])
    print(*ans)
