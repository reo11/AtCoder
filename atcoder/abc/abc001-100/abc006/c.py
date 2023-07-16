n, m = map(int, input().split())

ans = [0, 0, 0]

if m % 2 == 1:
    ans[1] = 1
    n -= 1

flag = False
for i in range(n + 1):
    ans[0] = n - i
    ans[2] = i
    if ans[0] * 2 + ans[1] * 3 + ans[2] * 4 == m:
        flag = True
        break
if flag:
    print(ans[0], ans[1], ans[2])
else:
    print("-1 -1 -1")
