N = int(input())
dims = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    dims[a - 1] += 1
    dims[b - 1] += 1

cnt = [0] * N
for x in dims:
    cnt[x] += 1

ans = []
vs = 0
for i, x in enumerate(cnt):
    if i >= 3:
        vs += (i + 1) * x
        ans += [i] * x

ans = [2] * ((N - vs) // 3) + ans
print(*ans)
