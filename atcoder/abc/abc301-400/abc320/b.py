s = list(input())
ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        si = s[i:j]
        if "".join(si) == "".join(list(reversed(si))):
            ans = max(ans, len(si))
print(ans)
