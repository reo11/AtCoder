n = int(input())
a = list(map(int, input().split()))
d = {}

for v in a:
    try:
        d[v] += 1
    except:
        d[v] = 1

ans = 0
for i, j in d.items():
    a = j - i if j >= i else j
    ans += a
print(ans)
