n = int(input())

points = [[0 for _ in range(n + 1)] for _ in range(3)]
cp = []
for i in range(1, n + 1):
    c, p = map(int, input().split())
    points[c][i] = p

# imos
for i in range(1, 3):
    v = 0
    for j in range(n + 1):
        v += points[i][j]
        points[i][j] = v

q = int(input())
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans1 = points[1][r] - points[1][l - 1]
    ans2 = points[2][r] - points[2][l - 1]
    ans.append(f"{ans1} {ans2}")
print("\n".join(ans))