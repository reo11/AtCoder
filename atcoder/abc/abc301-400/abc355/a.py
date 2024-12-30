a, b = map(int, input().split())

s = set([a, b])

if len(s) == 2:
    ans = {1, 2, 3} - s
    print(ans.pop())
else:
    print(-1)
