n = int(input())
a = [list(input()) for _ in range(n)]

inverses = {
    "-": "-",
    "W": "L",
    "L": "W",
    "D": "D",
}

ans = True

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if inverses[a[i][j]] != a[j][i]:
            ans = False
if ans:
    print("correct")
else:
    print("incorrect")
