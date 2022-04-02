import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += bisect.bisect_left(L, L[i] + L[j]) - 1 - j

print(ans)
