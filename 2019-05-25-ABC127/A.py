a, b = map(int, input().split())

ans = b

if 6 <= a <= 12:
    ans = b // 2
elif a < 6:
    ans = 0

print(ans)