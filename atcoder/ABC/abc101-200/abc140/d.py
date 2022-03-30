n, k = map(int, input().split())
s = str(input())

lr = 0
rl = 0
for i in range(n-1):
    if s[i:i+2] == "LR":
        lr += 1
    if s[i:i+2] == "RL":
        rl += 1
m = min(lr, rl)
ans = n - (lr + rl + 1) + (2 * min(m, k))

if k > m:
    if lr > rl and (s[0] == "L" or s[-1] == "R"):
        ans += 1
    if lr < rl and (s[0] == "R" or s[-1] == "L"):
        ans += 1
print(ans)