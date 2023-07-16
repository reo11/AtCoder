n = int(input())
s = input()

ans = ""
for i in range(len(s)):
    num = ord(s[i]) + n
    if num > ord("Z"):
        num %= ord("Z")
        num += ord("A") - 1
    ans += chr(num)
print(ans)
