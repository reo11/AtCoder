n, m = map(int, input().split())

ans = ['?' for _ in range(n)]
f = True
for i in range(m):
    s, c = map(int, input().split())
    if ans[s-1] != '?':
        if ans[s-1] != c:
            f = False
        else:
            ans[s-1] = c
    else:
        ans[s-1] = c
if n >= 2 and ans[0] == 0:
    f = False
output = ""

if f:
    if n >= 2 and ans[0] == '?':
        ans[0] = 1
    for i in range(n):
        if ans[i] == '?':
            ans[i] = 0
        output += str(ans[i])
    print(output)
else:
    print(-1)
