n, k = map(int, input().split())
s = list(input())

ans = []
for si in s:
    if si == "o" and k > 0:
        ans.append("o")
        k -= 1
    else:
        ans.append("x")
print("".join(ans))
