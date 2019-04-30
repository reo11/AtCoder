n, m, k = map(int, input().split())
a = list(map(int,input().split()))

# できるだけ大きくする
ans = 0
l = -1
r = l + m + 1
count = 0
while r < n:
    max_a = max(a[l+1:r])
    print(max_a)
    ans += max_a
    count += 1
    for i, v in enumerate(a[l+1:r][::-1]):
        if v == max_a:
            l += len(a[l+1:r][::-1]) - i
            r = l + m + 1
            break
if count < k:
    print(ans)
else:
    print(-1)