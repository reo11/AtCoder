n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = -1

# 短い場合
if n == 1 or m == 1:
    for a_i in range(n):
        for b_i in range(m):
            if abs(a[a_i] - b[b_i]) <= d:
                ans = max(ans, a[a_i] + b[b_i])
    print(ans)
    exit()

# 二分探索
for a_i in range(n):
    # 2通り考える必要がある
    # a_i - dとa_i + dの最も良いもの
    l = 0
    r = m - 1
    while r - l > 1:
        mid = (l + r) // 2
        if b[mid] < a[a_i] - d:
            l = mid
        else:
            r = mid
    for x in range(-2, 3):
        if r + x < 0 or r + x >= m:
            continue
        if abs(a[a_i] - b[r + x]) <= d:
            ans = max(ans, a[a_i] + b[r + x])
    l = 0
    r = m - 1
    while r - l > 1:
        mid = (l + r) // 2
        if b[mid] <= a[a_i] + d:
            l = mid
        else:
            r = mid
    for x in range(-2, 3):
        if l + x < 0 or l + x >= m:
            continue
        if abs(a[a_i] - b[l + x]) <= d:
            ans = max(ans, a[a_i] + b[l + x])
print(ans)