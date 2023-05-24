n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for a_i in a:
    for a_j in a:
        if a_i - a_j == x:
            ans += 1

if ans > 0:
    print("Yes")
else:
    print("No")
