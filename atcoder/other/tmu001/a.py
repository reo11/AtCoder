# たくさんの数式
s = str(input())

ans = 0
for i in range(2 ** (len(s)-1)):
    plus_l = []
    cal_l = []
    for j in range(len(s)):
        bit = 2 ** j
        if i & bit > 0:
            plus_l.append(j)
    if len(plus_l) == 0:
        cal_l = [int(s)]
    else:
        pre = 0
        for k in plus_l:
            cal_l.append(int(s[pre:k+1]))
            pre = k+1
        cal_l.append(int(s[pre:]))
    ans += sum(cal_l)

print(ans)


