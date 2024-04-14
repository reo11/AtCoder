n = int(input())

ans = []

for i in range(n):
    if (i + 1) % 3 == 0:
        ans.append("x")
    else:
        ans.append("o")
print("".join(ans))