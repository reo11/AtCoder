s = list(input())
for i in range(len(s) // 2):
    tmp = s[2 * i]
    s[2 * i] = s[2 * i + 1]
    s[2 * i + 1] = tmp
print("".join(s))
