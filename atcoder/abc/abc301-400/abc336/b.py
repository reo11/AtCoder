n = int(input())

ans = 0
while n > 0:
    if n & 1 == 0:
        ans += 1
    else:
        break
    n >>= 1
print(ans)