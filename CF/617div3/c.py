import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s = input().rstrip()
    d = {}
    x = 0
    y = 0
    d["0 0"] = 0
    ans = 10**9
    ans_s = ""
    for i, c in enumerate(s, start=1):
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        else:
            y -= 1
        p = "{} {}".format(x, y)
        try:
            if i - d[p] + 1 < ans:
                ans = i - d[p] + 1

                ans_s = "{} {}".format(d[p]+1, i)
                d[p] = i
            else:
                d[p] = i
        except:
            d[p] = i
    if ans == 10**9:
        print(-1)
    else:
        print(ans_s)