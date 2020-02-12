t = int(input())
for i in range(t):
    s = list(str(input().rstrip()))
    l = 0
    flag = False
    for i in range(len(s)):
        if s[i] == '1':
            l = i
            flag = True
            break

    r = len(s) - 1
    for i in reversed(range(len(s))):
        if s[i] == '1':
            r = i
            break

    ans = 0
    for i in range(l, r+1):
        if s[i] == '0':
            ans += 1
    cnt_0 = 0
    for i in s:
        if i == '0':
            cnt_0 += 1

    if cnt_0 == len(s):
        print(0)
    else:
        print(ans)
