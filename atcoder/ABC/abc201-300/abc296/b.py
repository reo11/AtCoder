s = []
for i in range(8):
    s.append(list(input()))
s = list(reversed(s))

ans = ""
for i in range(1, 9):
    for j in range(1, 9):
        j_str = chr(ord("a") + j - 1)
        if s[i - 1][j - 1] == "*":
            ans = f"{j_str}{i}"
print(ans)
