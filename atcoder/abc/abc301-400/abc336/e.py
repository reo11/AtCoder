n = int(input())

# その桁をxにしたときのmod pを前計算して後でmod pがゼロになるものを数える
# 下の桁からその桁以下を任意の数にしてmod pになるものの数を下から数える
# 9999...が桁和最大で、9 * 15 = 135

counts = [[0 for _ in range(135)] for _ in range(15)]

# 1桁目
for i in range(1, 135):
    for j in range(1, 10):
        counts[0][i] =

for i in range(1, 15):
    for j in range(135):
        counts[i][j] = counts[i - 1][j]
        counts[i][j] += counts[i - 1][(j - i * (10 ** (i - 1))) % 135]
    counts[i][i * (10 ** (i - 1)) % 135] += 1

