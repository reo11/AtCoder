n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

ans = float("inf")
for b_i in b:
    # 2分探索する
    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] < b_i:
            left = mid
        else:
            right = mid
    ans = min(ans, abs(a[left] - b_i))
    if right < n:
        ans = min(ans, abs(a[right] - b_i))

print(ans)
