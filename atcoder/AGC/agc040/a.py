s = input()

l = [0 for _ in range(len(s) + 1)]
for i in range(len(s)):
    if s[i] == "<":
        l[i + 1] = l[i] + 1

r = [0 for _ in range(len(s) + 1)]
for i in reversed(range(len(s))):
    if s[i] == ">":
        r[i] = r[i + 1] + 1

ans = 0
for i in range(len(s) + 1):
    ans += max(l[i], r[i])
print(ans)
