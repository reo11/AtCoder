n, m = map(int, input().split())
s = list(input())

ans = 0

current = [m, 0]  # 無地, ロゴ入り
for i in range(n):
    si = s[i]
    if si == "0":
        current[0] = m
        current[1] = 0
    elif si == "2":
        current[1] -= 1
    else:
        if current[0] > 0:
            current[0] -= 1
        else:
            current[1] -= 1
    ans = max(ans, abs(current[1]))
print(ans)
