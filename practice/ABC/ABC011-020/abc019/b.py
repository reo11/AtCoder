s = str(input())

pre = ""
count = 0
ans = ""
for i in range(len(s)):
    if pre == s[i]:
        count += 1
    else:
        if pre:
            ans += pre
            ans += str(count+1)
            count = 0
        pre = s[i]
ans += pre
ans += str(count+1)
print(ans)