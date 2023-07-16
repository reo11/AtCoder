s = list(str(input()))
re_s = s[::-1]

ans = 0
for i in range(len(s)):
    if s[i] != re_s[i]:
        ans += 1
print(ans // 2)
