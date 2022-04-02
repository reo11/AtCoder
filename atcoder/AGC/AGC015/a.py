n, a, b = map(int, input().split())

ans = 0
if n == 1:
    if a == b:
        ans = 1
    else:
        ans = 0
else:
    if a > b:
        ans = 0
    else:
        ans = (a + b * (n - 1)) - (a * (n - 1) + b) + 1
print(ans)
