s = list(input())

ans = -1
for i in range(len(s)):
    si = s[i]
    if si == "a":
        ans = i + 1
print(ans)
