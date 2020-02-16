n, k = map(int, input().split())
a = list(map(int, input().split()))
minus = [-x for x in a if x < 0]
plus = [x for x in a if x >= 0]

minus.sort()
plus.sort()

def cnt(x):
    ans = 0
    if x < 0:
        x = -x
        r = 0
        for num in minus[::-1]:
            while r < len(plus) and plus[r] * num < x:
                r += 1
            ans += len(plus) -  r
        return ans

    r = 0
    for num in minus[::-1]:
        if num * num <= x: ans -= 1
        while r < len(minus) and minus[r] * num <= x:
            r += 1
        ans += r
    r = 0
    for num in plus[::-1]:
        if num * num <= x: ans -= 1
        while r < len(plus) and plus[r] * num <= x:
            r += 1
        ans += r
    ans //= 2
    ans += len(minus) * len(plus)
    return ans

bottom = 0
top = 2*(10**18) + 2


while top - bottom > 1:
    mid = (top + bottom) // 2
    if cnt(mid - 10**18-1) < k:
        bottom = mid
    else:
        top = mid

print(int(top - 10**18-1))
