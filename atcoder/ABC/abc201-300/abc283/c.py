s = list(input())
n = len(s)


ans = 0
zero_count = 0
for i in range(n):
    if s[i] == "0":
        if zero_count == 0:
            zero_count += 1
        else:
            zero_count = 0
            ans += 1
    else:
        if zero_count == 1:
            zero_count = 0
            ans += 1
        ans += 1
if zero_count == 1:
    ans += 1

print(ans)