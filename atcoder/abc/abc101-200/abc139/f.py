from cmath import phase
from itertools import combinations

N = int(input())
xy = [complex(*map(int, input().split())) for _ in range(N)]
xy.sort(key=phase)
xy += xy
ans = 0
for i, j in combinations(range(N * 2 + 1), 2):
    if j - i <= N:
        ans = max(abs(sum(xy[i:j])), ans)
print(ans)
