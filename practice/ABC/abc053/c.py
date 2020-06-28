x = int(input())

ans = 0
if x % 11 == 0:
    ans = x // 11 * 2
elif x % 11 <= 6:
    ans = x // 11 * 2 + 1
else:
    ans = x // 11 * 2 + 2

print(ans)