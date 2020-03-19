s = list(str(input().rstrip()))
n = len(s)

ans = 2 * (n - 1)

for i in range(1, n - 1):
    ans += (n - 1)
    if s[i] == 'U':
        ans += i
    else:
        ans += n - i - 1

print(ans)
