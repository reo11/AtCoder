n, k = map(int, input().split())
p = list(map(int, input().split()))

e = []
for v in p:
    if v % 2 == 0:
        e.append(((v+1)*(v//2)) / v)
    else:
        e.append(((v+1)*(v//2) + (v+1) // 2) / v)

e_sum = [0]

for i in range(len(e)):
    e_sum.append(e_sum[i] + e[i])

ans = 0

for i in range(k, len(e_sum)):
    ans = max(ans, e_sum[i] - e_sum[i-k])

print(ans)
