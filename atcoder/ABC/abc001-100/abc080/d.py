import sys

input = sys.stdin.buffer.readline

n, C = map(int, input().split())
stc = []
max_t = 0
for i in range(n):
    s, t, c = map(int, input().split())
    max_t = max(max_t, t)
    stc.append([s, t, c])

len_imos = max_t + 1
imos = [[0 for _ in range(len_imos)] for _ in range(C)]
for i in range(n):
    s, t, c = stc[i]
    imos[c - 1][s - 1] += 1
    imos[c - 1][t] -= 1

for j in range(C):
    v = 0
    for i in range(len_imos):
        v += imos[j][i]
        imos[j][i] = v

ans = 0
v = 0
for i in range(len_imos):
    v = 0
    for c in range(C):
        v += 1 if imos[c][i] > 0 else 0
    ans = max(ans, v)
# print(imos)
print(ans)
