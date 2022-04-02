s = list(input())


def f(c):
    return ord(c) - ord("a") + 1


res = 0
for c in s:
    res += f(c)

ans = ""
while True:
    if len(ans) > 20:
        print("NO")
        exit()
    if list(ans) == s:
        break
    if res > 26:
        ans += "z"
        res -= 26
    elif res == 0:
        print(ans)
        exit()
    else:
        ans += chr(ord("a") - 1 + res)
        res = 0

res = 0
for c in s:
    res += f(c)

if s[0] == "a":
    ans = "b"
    res -= 2
else:
    ans = chr(ord(s[0]) - 1)
    res -= ord(s[0]) - ord("a")

while True:
    if len(ans) > 20 or res < 0:
        print("NO")
        exit()
    if res > 26:
        ans += "z"
        res -= 26
    elif res == 0:
        print(ans)
        exit()
    else:
        ans += chr(ord("a") - 1 + res)
        res = 0
