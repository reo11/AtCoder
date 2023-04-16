h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))

for i in range(h):
    for j in range(w - 1):
        if s[i][j] == "T" and s[i][j + 1] == "T":
            s[i][j] = "P"
            s[i][j + 1] = "C"


ans = []
for i in range(h):
    ans.append("".join(s[i]))
print("\n".join(ans))
