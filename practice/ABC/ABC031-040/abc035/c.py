n, q = map(int, input().split())
b = [0] * (n+1)
for i in range(q):
    l, r = map(int, input().split())
    b[l-1] += 1
    b[r] -= 1

cur = 0
ans = ""
for i in range(n):
    cur += b[i]
    if cur % 2 == 0:
        ans += "0"
    else:
        ans += "1"
print(ans)
