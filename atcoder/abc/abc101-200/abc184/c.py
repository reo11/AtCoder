r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

start = (r1, c1)
goal = (r2, c2)

# 必ず3手で到達できる
ans = 3

if start == goal:
    ans = 0
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    ans = 1
elif (
    abs((r1 + c1) - (r2 + c2)) <= 3
    or abs((r1 - c1) - (r2 - c2)) <= 3
    or abs(r1 - r2) + abs(c1 - c2) <= 6
    or (r1 + c1) % 2 == (r2 + c2) % 2
):
    ans = 2
else:
    ans = 3
print(ans)
