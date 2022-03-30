s = input()
codefest = "CODEFESTIVAL2016"
cnt = 0
for i in range(len(s)):
    if codefest[i] != s[i]:
        cnt += 1
print(cnt)