t = int(input())
ans = []
for i in range(t):
    a, b = map(int, input().split())
    out = ""
    if a == b:
        out = "0"
    elif a < b:
        if (a - b) % 2 == 1:
            out = "1"
        else:
            out = "2"
    else:
        if (a - b) % 2 == 0:
            out = "1"
        else:
            out = "2"
    ans.append(out)
print("\n".join(ans))
