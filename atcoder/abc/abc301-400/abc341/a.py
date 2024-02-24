n = int(input())
ans = []

for i in range(n):
    ans.append(1)
    ans.append(0)
ans.append(1)

print(*ans, sep="")