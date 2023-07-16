s = input()
ans = ""
for i in range(len(s)):
    ans += chr(ord(s[i]) + ord("A") - ord("a"))
print(ans)
