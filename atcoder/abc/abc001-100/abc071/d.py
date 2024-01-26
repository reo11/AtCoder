MOD = 10**9 + 7

n = int(input())
s1 = input()
s2 = input()
ans = 1

if s1[0] == s2[0]:
    i = 1
    pre_pat = 0
    ans = 3
else:
    i = 2
    pre_pat = 1
    ans = 6

t = [[2, 2], [1, 3]]
while True:
    if i >= n:
        break
    if s1[i] == s2[i]:
        pat = 0
        i += 1
    else:
        pat = 1
        i += 2
    ans *= t[pre_pat][pat]
    ans %= MOD
    # print(pre_pat, pat, ans, i)
    pre_pat = pat
print(ans)
