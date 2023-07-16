n = int(input())
s = input()

ans = ""
for i in range(n):
    ans += s[i] + s[i]
print(ans)
