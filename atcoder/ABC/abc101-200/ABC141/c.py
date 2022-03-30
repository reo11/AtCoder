n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

points = [k-q] * n
ans = []
for i in a:
    points[i-1] += 1

for i in range(n):
    if points[i] <= 0:
        ans.append("No")
    else:
        ans.append("Yes")

print("\n".join(ans))
