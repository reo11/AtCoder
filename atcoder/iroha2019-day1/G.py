n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# できるだけ大きくする
ans = 0
left = -1
right = left + m + 1
count = 0
while right < n:
    max_a = max(a[left + 1 : right])
    print(max_a)
    ans += max_a
    count += 1
    for i, v in enumerate(a[left + 1 : right][::-1]):
        if v == max_a:
            left += len(a[left + 1 : right][::-1]) - i
            right = left + m + 1
            break
if count < k:
    print(ans)
else:
    print(-1)
