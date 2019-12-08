n = int(input())
xy = []
for i in range(n):
    a = int(input())
    l = []
    for j in range(a):
        x, y = map(int, input().split())
        l.append((x, y))
    xy.append(l)

# ビット全探索
bit = 0
ans = 0
for X in range(2 ** n):
    # 1010など
    flag = False
    count = 0
    for num in range(n):
        f = True
        if X & (2 ** num) >= 1:
            for x, y in xy[num]:
                t = 1 if X & 2 ** (x-1) >= 1 else 0
                if t != y:
                    f = False
                    break
            if f == False:
                count = 0
                break
            count += 1
    ans = max(count, ans)
print(ans)