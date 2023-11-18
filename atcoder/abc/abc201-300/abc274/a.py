a, b = map(int, input().split())
ans = str(round(b / a, 3))
if len(ans) < 5:
    ans += '0' * (5 - len(ans))
print(ans)