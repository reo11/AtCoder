n, k = map(int, input().split())
v = list(map(int, input().split()))
# DPでいけそうだぞい
# 左右のDP
dp_l = [0] * (k + 2)
dp_r = [0] * (k + 2)

for i in range(1, k):
    dp_l[i + 1] = max(dp_l[i] + v[i], dp_l[i - 1])

v = v[::-1]
for i in range(1, k):
    dp_r[i + 1] = max(dp_r[i] + v[i], dp_r[i - 1])

print(dp_l, dp_r)
