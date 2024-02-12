import math

n, a, b = map(int, input().split())

# 包除原理
# 1からnの和 - aの倍数の合計 - bの倍数の合計 + a*bの倍数の合計

# 1からnの和
s = n * (n + 1) // 2
# aの倍数の合計
sa = a * (n // a) * (n // a + 1) // 2
# bの倍数の合計
sb = b * (n // b) * (n // b + 1) // 2
# a*bの倍数の合計
ab = math.lcm(a, b)
sab = ab * (n // ab) * (n // ab + 1) // 2

print(s - sa - sb + sab)
