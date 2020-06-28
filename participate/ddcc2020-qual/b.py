n = int(input())
a = list(map(int, input().split()))

l = 0
r = 0
l_num = 0
r_num = -1
while n > 1:
    if l <= r:
        l += a[l_num]
        l_num += 1
    else:
        r += a[r_num]
        r_num -= 1
    n -= 1

ans = min(abs(r - (l + a[l_num])), abs(l - (r + a[r_num])))

print(ans)
