INF = float("inf")
m = int(input())
s = []
for _ in range(3):
    s.append(list(map(int, list(input()))))

for i in range(3):
    s[i] = s[i] + s[i] + s[i]

ans = INF
for target_number in range(10):
    for first, second, third in [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]:
        num = 0
        for t in range(3 * m):
            if num == 0 and s[first][t] == target_number:
                num += 1
            elif num == 1 and s[second][t] == target_number:
                num += 1
            elif num == 2 and s[third][t] == target_number:
                num += 1
                ans = min(ans, t)
                break
# print(s)
if ans == INF:
    print(-1)
else:
    print(ans)
