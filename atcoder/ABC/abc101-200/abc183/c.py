from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for v in permutations(range(1, n)):
    v = [0] + list(v) + [0]
    time = 0
    for i in range(1, len(v)):
        time += t[v[i-1]][v[i]]
    if time == k:
        ans += 1
    # print(v, time)
print(ans)
