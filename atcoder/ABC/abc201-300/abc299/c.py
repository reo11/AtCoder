n = int(input())
s = input()

ans = -1
flag = False
count = 0
for i in range(n):
    if s[i] == "o":
        count += 1
    else:
        if count > 0 and (s[i] == "-" or flag):
            ans = max(ans, count)
        flag = True
        count = 0
if count > 0 and flag:
    ans = max(ans, count)
print(ans)