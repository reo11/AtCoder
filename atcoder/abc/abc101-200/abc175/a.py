s = input()
ans = 0
cnt = 0
for i in range(3):
    if s[i] == "S":
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
