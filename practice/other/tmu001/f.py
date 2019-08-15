# 東京都
q = int(input())

ans = []
for i in range(q):
    s = str(input())
    count = 0
    j = 0
    while j < len(s) - 4:
        if s[j:j+5] == "kyoto":
            count += 1
            j += 5
        elif s[j:j+5] == "tokyo":
            count += 1
            j += 5
        else:
            j += 1
    ans.append(str(count))
print("\n".join(ans))