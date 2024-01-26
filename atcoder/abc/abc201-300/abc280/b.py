n = int(input())
s = list(map(int, input().split()))

ans = [0]

for si in range(n):
    if si > 0:
        ans.append(s[si] - s[si - 1])
    else:
        ans.append(s[si])
ans = ans[1:]
print(*ans, sep=" ")
