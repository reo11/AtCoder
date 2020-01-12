n = int(input())
s = str(input())

ans = 0
for i in range(len(s) - 2):
    if s[i:i+3] == "ABC":
        ans += 1
print(ans)