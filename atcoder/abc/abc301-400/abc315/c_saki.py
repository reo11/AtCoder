N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

S = sorted(S, key=lambda x: x[1], reverse=True)

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if S[i][0] != S[j][0]:
            if ans < S[i][1] + S[j][1]:
                ans = S[i][1] + S[j][1]
            break
        else:
            if ans < S[i][1] + S[j][1] // 2:
                ans = S[i][1] + S[j][1] // 2

print(ans)
