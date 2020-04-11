N, C = list(map(int, input().split()))

D = []

for i in range(N):
    D.append(list(map(int, input().split())))

R = [[0, 0] for i in range(N + 1)]
cnt = 0
ma = 0
rma = 0
R[0][0] = -1
for i in range(N):
    cnt += D[i][1]
    if cnt - D[i][0] > ma:
        ma = cnt - D[i][0]
    if cnt - D[i][0] * 2 > rma:
        rma = cnt - D[i][0] * 2
    R[i + 1] = [ma, rma]

cnt = 0
Ans = R[N][0]
tmp = 0
for i in range(N - 1, -1, -1):
    cnt += D[i][1]
    tmp = C - D[i][0]
    tmp2 = cnt - tmp * 2 + R[i][0]
    tmp2 = max(tmp2, cnt - tmp + R[i][1])
    if tmp2 > Ans:
        Ans = tmp2

print(Ans)
