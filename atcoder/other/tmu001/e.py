# おつり

n = int(input())
a = 1000 - n
left = [500, 100, 50, 10, 5, 1]
ans = 0

for v in left:
    if a // v > 0:
        ans += a // v
        a %= v

print(ans)
