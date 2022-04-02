n = int(input())
a = list(map(int, input().split()))

left = 0
right = 0
l_num = 0
r_num = -1
while n > 1:
    if left <= right:
        left += a[l_num]
        l_num += 1
    else:
        right += a[r_num]
        r_num -= 1
    n -= 1

ans = min(abs(right - (left + a[l_num])), abs(left - (right + a[r_num])))

print(ans)
