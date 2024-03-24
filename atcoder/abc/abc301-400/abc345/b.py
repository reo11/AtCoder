x = int(input())

ans = x // 10
if x % 10 > 0:
    ans += 1
print(ans)