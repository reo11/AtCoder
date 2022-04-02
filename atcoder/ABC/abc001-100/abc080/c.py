n = int(input())

f = []
for i in range(n):
    f.append(list(map(int, input().split())))

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

# bit全探索
ans = -(10 ** 10)

for i in range(1, 2 ** 10):
    l = [0 for _ in range(10)]
    for j in range(10):
        if i & 2 ** j > 0:
            l[j] = 1
    score = 0
    for j in range(n):
        count = 0
        for k in range(10):
            if f[j][k] == l[k] == 1:
                count += 1
        score += p[j][count]
    ans = max(ans, score)
print(ans)
