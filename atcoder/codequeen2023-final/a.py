s = list(input())
c = input()

ans = ""
for s_i in s:
    ans += s_i
    if s_i == c:
        ans += s_i
print(ans)
