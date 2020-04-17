from collections import defaultdict

n, p = map(int, input().split())
s = list(map(int, list(input())))

ans = 0
if p == 2:
    for i in range(n):
        if s[i] % 2 == 0:
            ans += (i + 1)
elif p == 5:
    for i in range(n):
        if s[i] % 5 == 0:
            ans += (i + 1)
else:
    
